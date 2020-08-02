"""Copyright Header Details

Copyright
---------
    Copyright (C) Guya , PLC - All Rights Reserved (As Of Pending...)
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential

LICENSE
-------
    This file is subject to the terms and conditions defined in
    file 'LICENSE.txt', which is part of this source code package.

Authors
-------
    * [Simon Belete](https://github.com/Simonbelete)

Project
-------
    * Name:
        - Guya E-commerce & Guya Express
    * Sub Project Name:
        - Cart service for Guya microservices
    * Description
        - Cart mangement service
"""


"""This module contains class whose instances will be used to
load the settings according to the running environment. """

import os


class Config:
    """Class containing the default settings for all environments.

    Constants:
    ---------
        SQLALCHEMY_TRACK_MODIFICATIONS (boolean): signals to get notified
        before and after changes are committed to the database.
    """

    DEBUG = False

    TESTING = False

    MONGODB_DB = os.environ.get('MONGODB_DB')
    
    MONGODB_HOST = os.environ.get('MONGODB_HOST')

    MONGODB_PORT = int(os.environ.get('MONGODB_PORT'))

    MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')

    MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')


class Prodconfig(Config):
    """Class containing the settings of the production environment .
    It load some values from the environment to be used in the internal Flask config.

    Constants:
    ---------
        SECRET_KEY (str): The application secret key used to encrypt your cookies.
    """

    SECRET_KEY = os.getenv('SECRET_KEY')

class DevConfig(Config):
    """Class containing the settings of the development environment.
    It uses the dotenv library to load some values from the .env file to environment.
    After that, theses values are load from the environment to be use in the internal Flask config.

    Constants:
    ---------
        SECRET_KEY (str): The application secret key used to encrypt your cookies.
    """

    SECRET_KEY = 'dev'

    DEBUG = True


class TestConfig(Config):
    """Class containing the settings of the production environment .
    It load some values from the environment to be used in the internal Flask config."""

    TESTING = True


config_by_name = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=Prodconfig
)
