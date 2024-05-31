#!/usr/bin/env python3
"""
Defines a flask app
"""
from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def welcome() -> str:
    """
    Route to welcome.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register() -> str:
    """
    Route to register users.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
