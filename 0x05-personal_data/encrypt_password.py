#!/usr/bin/env python3
""" Encrypting pswds with bcrypt """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


def is_valid(hash_password: bytes, password: str) -> bool:
    """ Checks if hashed and unhashed pswds are same
    Returns bool
    """
    if bcrypt.checkpw(password.encode('utf8'), hash_password):
        return True
    else:
        return False
