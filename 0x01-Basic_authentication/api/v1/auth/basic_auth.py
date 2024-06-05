#!/usr/bin/env python3
"""Define the BasicAuth class"""
from .auth import Auth
from base64 import b64decode, decode
from io import StringIO


class BasicAuth(Auth):
    """Basic authentication class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
            for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]


    def decode_base64_authorization_header(self,
            base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
            base64_authorization_header:
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            b64decode(base64_authorization_header)
        except:
            return None
        out = StringIO()
        decode(StringIO(base64_authorization_header), out)
        return out.readline()
