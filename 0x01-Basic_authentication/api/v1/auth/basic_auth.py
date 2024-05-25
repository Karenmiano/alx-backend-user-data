#!/usr/bin/env python3
"""
BasicAuth module.
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Class to implement BasicAuth.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extract encoded credentials from Authorization header.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[-1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        Decode token in authorization header.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            byte_str = base64.b64decode(base64_authorization_header)
            str_decode = byte_str.decode("utf-8")

            return str_decode
        except binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract user credentials.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        credentials = tuple(decoded_base64_authorization_header.split(":"))

        return credentials
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns a user object based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        
        User.load_from_file()
        users = User.search({"email": user_email})

        if len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user