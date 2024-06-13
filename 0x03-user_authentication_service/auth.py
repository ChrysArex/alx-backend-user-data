#!/usr/bin/env python3
"""Define useful functions to enable security and authentication
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password):
    """Hash and salt the password argument"""
    return bcrypt.hashpw(bytes(password, "utf8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initialize the new object"""
        self._db = DB()

    def register_user(self, email, password) -> User:
        """Register a new user if he doesn't exist yet"""
        session = self._db._session
        check = session.query(User).filter_by(email=email).first()
        if check:
            raise ValueError("User {} already exists".format(email))
        new = User(email=email, hashed_password=_hash_password(password))
        session.add(new)
        session.commit()
        return new
