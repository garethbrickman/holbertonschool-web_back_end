#!/usr/bin/env python3
""" Route module for the API """
from flask import Flask, jsonify, request

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
    Registers new user with email and pswd in request form-data,
    or finds if user already registered based on email
    Return:
      - JSON payload
    """

    """ form-data uses request.form, body JSON uses request.get_json() """
    form_data = request.get_json()

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:

        data_email = form_data["email"]
        data_pswd = form_data["password"]

        try:
            new_user = AUTH.register_user(data_email, data_pswd)
            return jsonify({
                "email": new_user.email,
                "message": "user created"
            }), 201
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
