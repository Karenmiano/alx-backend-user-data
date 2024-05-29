#!/usr/bin/env python3
"""
Defines class SessionExpAuth.
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class - sets expiration duration for session
    """
    def __init__(self):
        """
        Set the session duration.
        """
        try:
            SESSION_DURATION = int(getenv('SESSION_DURATION'))
        except Exception:
            SESSION_DURATION = 0
        self.session_duration = SESSION_DURATION

    def create_session(self, user_id=None):
        """
        Create session_id for User user_id.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the user_id from session_id.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        session_details = self.user_id_by_session_id.get(session_id)
        if session_details is None:
            return None

        if self.session_duration <= 0:
            return session_details.get("user_id")

        created_at = session_details.get("created_at")
        if created_at is None:
            return None
        allowed_window = created_at + timedelta(seconds=self.session_duration)
        if allowed_window < datetime.now():
            return None

        return session_details.get("user_id")
