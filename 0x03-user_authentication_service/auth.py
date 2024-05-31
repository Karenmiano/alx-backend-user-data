#!/usr/bin/env python3
"""
Module for authentication.
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """
    Return hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def _generate_uuid() -> str:
    """
    Return a string representation of a uuid.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Set up a db instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user and returns the created user object.
        """
        try:
            find_user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password).decode("utf-8")
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check login credentials.
        """
        try:
            find_user = self._db.find_user_by(email=email)
            hashed_password = find_user.hashed_password.encode("utf-8")
            return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create session_id for user in database.
        """
        find_user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        self._db.update_user(find_user.id, session_id=session_id)
        return session_id
