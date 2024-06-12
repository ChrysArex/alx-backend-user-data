#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """save and returns a User object"""
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users table as filtered
            by the method’s input arguments
        """
        for i in dict(kwargs).keys():
            try:
                User().__getattribute__(i)
            except AttributeError:
                raise InvalidRequestError
        session = self.__session
        row = session.query(User).filter_by(**kwargs).first()
        if row is None:
            raise NoResultFound
        return row

    def update_user(self, user_id, **kwargs) -> None:
        """Find user with id == user_id and update his informations
           according to **kwargs
        """
        session = self._session
        for i in dict(kwargs).keys():
            try:
                User().__getattribute__(i)
            except AttributeError:
                raise ValueError
        usr = self.find_user_by(id=user_id)
        for new in dict(kwargs).keys():
            usr.__setattr__(new, kwargs.get(new))
        session.commit()
