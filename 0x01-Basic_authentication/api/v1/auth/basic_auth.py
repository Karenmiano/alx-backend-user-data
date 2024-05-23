#!/usr/bin/env python3
"""
BasicAuth module.
"""
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self,
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
