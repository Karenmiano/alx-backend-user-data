#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
# user_email = str(uuid.uuid4())
# print(user_email)
# user_clear_pwd = str(uuid.uuid4())
# print(user_clear_pwd)
# user = User()
# user.email = user_email
# user.first_name = "Jane"
# user.last_name = "Dylan"
# user.password = user_clear_pwd
# print("New user: {}".format(user.display_name()))
# user.save()

# """ Retreive this user via the class BasicAuth """

# a = BasicAuth()

# u = a.user_object_from_credentials(None, None)
# print(u.display_name() if u is not None else "None")

# u = a.user_object_from_credentials(89, 98)
# print(u.display_name() if u is not None else "None")

# u = a.user_object_from_credentials("email@notfound.com", "pwd")
# print(u.display_name() if u is not None else "None")

# u = a.user_object_from_credentials(user_email, "pwd")
# print(u.display_name() if u is not None else "None")

a = BasicAuth()
u = a.user_object_from_credentials("5c34ad76-b763-48c7-ba06-cf41eadc71af", "4679ff29-6e73-4604-95c0-fb587a469495")
print(u.display_name() if u is not None else "None")

