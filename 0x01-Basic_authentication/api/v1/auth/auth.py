#!/usr/bin/env python3
""" Module of Auth class
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from typing import List, TypeVar


class Auth():
    """class to manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns True if the path is not in the list of
            strings excluded_paths
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path_w = path + '/'
        else:
            path_w = path[:-1]
        for i in excluded_paths:
            if i == path or i == path_w:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None
        """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None
        """
        return None
