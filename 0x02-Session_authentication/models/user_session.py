#!/usr/bin/env python3
"""
Defines UserSession class
"""
from models.base import Base


class UserSession(Base):
    """
    UserSession class to store user sessions in file.
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize Usersession instance.
        """
        super().__init__(*args, **kwargs)
        self.session_id = kwargs.get("session_id")
        self.user_id = kwargs.get("user_id")
