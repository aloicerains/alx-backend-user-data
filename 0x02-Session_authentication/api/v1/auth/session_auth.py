#!/usr/bin/env python3
"""SessionAuth
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import uuid


class SessionAuth(Auth):
    """Implements session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates session id for user_id"""
        if user_id:
            if type(user_id) is str:
                sess_id = str(uuid.uuid4())
                self.user_id_by_session_id[sess_id] = user_id
                return sess_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns the user ID based on the Session Id
        """
        if session_id:
            if type(session_id) is str:
                return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns a User instance based on cookie value
        """
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_for_session_id(session_id)
            return User.get(str(user_id))

    def destroy_session(self, request=None):
        """Deletes the user session
        """
        if request:
            sess_id = self.session_cookie(request)
            if sess_id:
                if self.user_id_for_session_id(sess_id):
                    del self.user_id_by_session_id[sess_id]
                    return True
        return False
