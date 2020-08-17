#!/usr/bin/env python3
""" Authentication
"""
from db import DB
from user import User

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ Takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Instance """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers and returns a new user if email isn't listed"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {:s} already exists".format(email))
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
