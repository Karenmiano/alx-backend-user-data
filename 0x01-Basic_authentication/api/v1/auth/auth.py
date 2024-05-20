#!/usr/bin/env python3
"""
Authentication module.
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """
    Defines the auth class.
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
    
    def authorization_header(self, request=None) -> str | None:
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
