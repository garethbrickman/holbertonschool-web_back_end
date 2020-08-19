#!/usr/bin/env python3
""" Route module for the API """
from flask import Flask, jsonify, request, abort, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /status
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users
    Registers new user with email and pswd in x-www-form-urlencoded request,
    or finds if user already registered based on email
    Return:
      - JSON payload
    """

    """ form-data uses request.form, body JSON uses request.get_json() """
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        try:
            new_user = AUTH.register_user(email, pswd)
            return jsonify({
                "email": new_user.email,
                "message": "user created"
            })
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions
    Creates new session for user, stores as cookie
    Email and pswd fields in x-www-form-urlencoded request
    Return:
      - JSON payload
    """
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        if AUTH.valid_login(email, pswd) is False:
            abort(401)
        else:
            session_id = AUTH.create_session(email)
            response = jsonify({
                "email": email,
                "message": "logged in"
                })
            response.set_cookie('session_id', session_id)

            return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> None:
    """ DELETE /sessions
    Destroys session by finding session_id (key in cookie)
    Return:
      - Redirects user to status route (GET /)
    """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect(url_for('status'))
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
