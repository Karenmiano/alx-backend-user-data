#!/usr/bin/env python3
"""
Defines class SessionDBAuth
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
import uuid


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth - stores session in file.
    """
    def create_session(self, user_id=None):
        """
        Creates and stores session for User user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns User id based on session_id
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        UserSession.load_from_file()
        user_sessions = UserSession.search({"session_id": session_id})
        if len(user_sessions) == 0:
            return None
        user_session = user_sessions[0]
        return user_session.user_id
        
    def destroy_session(self, request=None):
        """
        Destroy current user session.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        user = UserSession.get(user_id)
        user.remove()
        return True
      