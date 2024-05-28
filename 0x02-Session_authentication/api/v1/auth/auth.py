#!/usr/bin/env python3
"""
Auth module.
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Auth BaseClass for all authentication systems.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if path requires authentication.
        If not in excluded_paths.
        """
        if path is None or excluded_paths is None:
            return True
        path = path if path[-1] == '/' else path + '/'
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves value passed in Authorization header in request.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        """
        return None

    def session_cookie(self, request=None):
        """
        Retrieves session_id from session cookies
        """
        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")
        session_id = request.cookies.get(SESSION_NAME)

        return session_id
