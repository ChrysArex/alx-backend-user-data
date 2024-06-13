#!/usr/bin/env python3
"""Set up a simple flask app"""


from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """greet users"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """register a user in the app"""
    try:
        AUTH.register_user(request.form.get("email"),
                           request.form.get("password"))
    except ValueError:
        return jsonify({"message": "email already registered"})
    else:
        return {"email": "{}".format(request.form.get("email")),
                "message": "user created"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
