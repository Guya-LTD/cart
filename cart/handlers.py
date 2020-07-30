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


"""This module registers the error handler on the application."""


from flask import jsonify
from werkzeug.exceptions import HTTPException, default_exceptions


def register_handler(app):
    """Registers the error handler is a function to common error HTTP codes

    Parameters:
    ----------
        app (flask.app.Flask): The application instance.
    """

    def generic_http_error_handler(error):
        """Deal with HTTP exceptions.

        Parameters:
        ----------
            error (HTTPException): A werkzeug.exceptions.BadRequest exception object.

        Returns:
        -------
            A flask response object.
        """
        if isinstance(error, HTTPException):
            result = {
                'code': error.code,
                'description': error.description,
                'type': 'HTTPException',
                'message': str(error)}
        else:
            result = {
                'code': 500,
                'description': 'Internal Server Error',
                'type': 'Other Exceptions',
                'message': str(error)}

        #logger.exception(str(error), extra=result.update(EXTRA))
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    # register http code errors
    for code in default_exceptions.keys():
        app.register_error_handler(code, generic_http_error_handler)
