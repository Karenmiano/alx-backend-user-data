#!/usr/bin/env python3
"""
Defines class SessionAuth
"""
from api.v1.auth.auth import Auth
import uuid
from os import getenv


class SessionAuth(Auth):
    """
    SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User id based on session_id
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        user_id = SessionAuth.user_id_by_session_id.get(session_id)

        return user_id

    def session_cookie(self, request=None):
        """
        Retrieves session_id from session cookies
        """
        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")
        session_id = request.cookies.get(SESSION_NAME)

        return session_id
