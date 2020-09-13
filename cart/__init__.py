# -*- coding: utf-8 -*-

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


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style


This module contains the factory function 'create_app' that is
responsible for initializing the application according
to a previous configuration.
"""

import os
from flask import Flask
from dotenv import load_dotenv

from .blueprint.v1 import *
from .config import config_by_name
from .handlers import register_handler

# import all controllers
from cart.controller.v1 import cart_controller, item_controller

# const vars
__version__ = '0.3.0'
__email__ = 'simonbelete@gmail.com'
__title__ = 'Cart service for Guya microservices'
__author__ = 'Simon Belete'
__keywords__ = ''
__repo_name__ = 'Cart service for Guya microservices'
__description__ = 'Cart mangement service'
__project_name__ = 'Cart service for Guya microservices'


def create_app(test_config: dict = {}) -> Flask:
    """This function is responsible to create a Flask instance according
    a previous setting passed from environment. In that process, it also
    initialise the database source.

    Parameters:
    ----------
        test_config (dict): settings coming from test environment

    Returns:
    -------
        flask.app.Flask: The application instance
    """

    app = Flask(__name__, instance_relative_config=True)

    app.app_context().push()

    load_dotenv()
    load_config(app)
    register_handler(app)
    
    init_database(app)
    init_blueprints(app)

    return app


def load_config(app: Flask) -> None:
    """Load the application's config

    Parameters:
    ----------
        app (flask.app.Flask): The application instance Flask that'll be running
        test_config (dict):
    """

    app.config.from_object(config_by_name[os.getenv('ENV')])


def init_database(app) -> None:
    """Responsible for initializing and connecting to the database
    to be used by the application.

    Parameters:
    ----------
        app (flask.app.Flask): The application instance Flask that'll be running
    """

    from .database import init
    init(app)


def init_blueprints(app: Flask) -> None:
    """Registes the blueprint to the application.

    Parameters:
    ----------
        app (flask.app.Flask): The application instance Flask that'll be running
    """

    # register version based blueprint group

    app.register_blueprint(blueprint)
