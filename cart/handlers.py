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
        - Branch Service
    * Description
        - Branch location and details service
"""


"""This module registers the error handler on the application."""


from flask import jsonify
from pymongo import errors as pymongoErrors
from werkzeug.exceptions import HTTPException, default_exceptions
from requests.exceptions import RequestException

from .database import db
from .log import log_exception


def register_handler(app) -> None:
    """Registers the error handler is a function to common error HTTP codes

    Parameters:
    ----------
        app (flask.app.Flask): The application instance.
    """

    ################################################################
    #
    # generic error handlers
    #
    ################################################################

    # http codes generic error handler
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
                'status_code': error.code,
                'status': error.description,
                'extra_message': "Flask Http Exception",
                'error': {
                    'message': str(error),
                    'type': 'HTTPException'
                }}
        else:
            result = {
                'status_code': 500,
                'status': 'Internal Server Error',
                'extra_message': "Flask Http Exception",
                'error': {
                    'message': str(error),
                    'type': 'Exception'
                }}

        log_exception(error = error, extra = result)
        resp = jsonify(result)
        resp.status_code = result['status_code']
        return resp
 

     ## Mongoengine Exception handlers
    def mongoengine_generic_error_handler(error, code = 500):
        """Deal with mongoengine exceptions.

        Parameters:
        ----------
            error (db.Exception): A mongoengine.exceptions exception object.

            code int: An HTTP status code.

        Returns:
        -------
            A flask response object.
        """
        # formatting the exception
        result = {
            'status_code': 500,
            'status': 'Internal Server Error',
            'extra_message': "Mongoengine Exception",
            'error': {
                'message': str(error),
                'type': 'mongoengine.errors'
            }}

        # logg exception
        log_exception(error = error, extra = result)
        resp = jsonify(result)
        resp.status_code = 500
        return resp


    ## pymongo exception handlers
    def pymongo_generic_error_handler(error):
        """Deal with mongoengine exceptions.

        Parameters:
        ----------
            error (pymongo.errors): A pymongo.errors exception object.

        Returns:
        -------
            A flask response object.
        """
        # formatting the exception
        result = {
            'status_code': 500, 
            'status': 'Internal Server Error',
            'extra_message': "PyMongoengine Exception",
            'error': {
                'message': str(error),
                'type': 'pymongo.errors'
            }}

        # logg exception
        log_exception(error = error, extra = result)
        resp = jsonify(result)
        resp.status_code = 500
        return resp

    
    ## requests generic exception handler
    def requests_generic_error_handler(error):
        """Deal with requests exceptions.

        Parameters:
        ----------
            error (requests.exceptions.RequestException): A requests.exceptions.RequestException exception object.

        Returns:
        -------
            A flask response object.
        """
        # formatting the exception
        result = {
            'status_code': 500, 
            'status': 'Internal Server Error',
            'extra_message': "Requests Exception",
            'error': {
                'message': str(error),
                'type': 'requests.exceptions.RequestException'
            }}

        # logg exception
        log_exception(error = error, extra = result)
        resp = jsonify(result)
        resp.status_code = 500
        return resp


    # pymongo handlers
    def pymongo_auto_reconnect_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_bulkwrite_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_collection_invalid_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_configuration_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_connection_failure_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_cursor_not_found_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_document_too_large_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_duplicate_key_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_encryption_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_exceede_max_waiters_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_execution_timeout_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_invalid_name_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_invalid_operation_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_invalid_uri_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_network_timeout_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_not_master_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_operation_failure_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_protocol_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_pymongo_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_server_selection_timeout_error_handler(error): 
        return pymongo_generic_error_handler(error)

    def pymongo_wtimeout_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_write_concern_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_write_error_handler(error):
        return pymongo_generic_error_handler(error)


    # mongoengine handlers
    def mongoengine_not_registered_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_invalid_document_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_lookup_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_does_not_exist_error_handler(error):
        return mongoengine_generic_error_handler(error = error, code = 204)

    def mongoengine_multiple_objects_returned_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_invalid_query_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_operation_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_not_unique_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_bulk_write_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_file_doesnot_exist_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_validation_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_save_condition_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_deprecated_error_handler(error):
        return mongoengine_generic_error_handler(error)


    ################################################################
    #
    # register exception handlers to flask
    #
    ################################################################

    # register http status codes
    for code in default_exceptions.keys():
        app.register_error_handler(code, generic_http_error_handler)

    # pymongoexceptions
    app.register_error_handler(pymongoErrors.AutoReconnect, pymongo_auto_reconnect_error_handler)
    app.register_error_handler(pymongoErrors.BulkWriteError, pymongo_bulkwrite_error_handler)
    app.register_error_handler(pymongoErrors.CollectionInvalid, pymongo_collection_invalid_error_handler)
    app.register_error_handler(pymongoErrors.ConfigurationError, pymongo_configuration_error_handler)
    app.register_error_handler(pymongoErrors.ConnectionFailure, pymongo_connection_failure_error_handler)
    app.register_error_handler(pymongoErrors.CursorNotFound, pymongo_cursor_not_found_error_handler)
    app.register_error_handler(pymongoErrors.DocumentTooLarge, pymongo_document_too_large_error_handler)
    app.register_error_handler(pymongoErrors.DuplicateKeyError, pymongo_duplicate_key_error_handler)
    app.register_error_handler(pymongoErrors.EncryptionError, pymongo_encryption_error_handler)
    app.register_error_handler(pymongoErrors.ExceededMaxWaiters, pymongo_exceede_max_waiters_error_handler)
    app.register_error_handler(pymongoErrors.ExecutionTimeout, pymongo_execution_timeout_error_handler)
    app.register_error_handler(pymongoErrors.InvalidName, pymongo_invalid_name_error_handler)
    app.register_error_handler(pymongoErrors.InvalidOperation, pymongo_invalid_operation_error_handler)
    app.register_error_handler(pymongoErrors.InvalidURI, pymongo_invalid_uri_error_handler)
    app.register_error_handler(pymongoErrors.NetworkTimeout, pymongo_network_timeout_error_handler)
    app.register_error_handler(pymongoErrors.NotMasterError, pymongo_not_master_error_handler)
    app.register_error_handler(pymongoErrors.OperationFailure, pymongo_operation_failure_error_handler)
    app.register_error_handler(pymongoErrors.ProtocolError, pymongo_protocol_error_handler)
    app.register_error_handler(pymongoErrors.PyMongoError, pymongo_pymongo_error_handler)
    app.register_error_handler(pymongoErrors.ServerSelectionTimeoutError, pymongo_server_selection_timeout_error_handler)
    app.register_error_handler(pymongoErrors.WTimeoutError, pymongo_wtimeout_error_handler)
    app.register_error_handler(pymongoErrors.WriteConcernError, pymongo_write_concern_error_handler)
    app.register_error_handler(pymongoErrors.WriteError, pymongo_write_error_handler)


    # register mongoengine exceptions    
    app.register_error_handler(db.NotRegistered, mongoengine_not_registered_error_handler)
    app.register_error_handler(db.InvalidDocumentError, mongoengine_invalid_document_error_handler)
    app.register_error_handler(db.LookUpError, mongoengine_lookup_error_handler)
    app.register_error_handler(db.DoesNotExist, mongoengine_does_not_exist_error_handler)
    app.register_error_handler(db.MultipleObjectsReturned, mongoengine_multiple_objects_returned_error_handler)
    app.register_error_handler(db.InvalidQueryError, mongoengine_invalid_query_error_handler)
    app.register_error_handler(db.OperationError, mongoengine_operation_error_handler)
    app.register_error_handler(db.NotUniqueError, mongoengine_not_unique_error_handler)
    app.register_error_handler(db.BulkWriteError, mongoengine_bulk_write_error_handler)
    app.register_error_handler(db.FieldDoesNotExist, mongoengine_file_doesnot_exist_error_handler)
    app.register_error_handler(db.ValidationError, mongoengine_validation_error_handler)
    app.register_error_handler(db.SaveConditionError, mongoengine_save_condition_error_handler)
    app.register_error_handler(db.DeprecatedError, mongoengine_deprecated_error_handler)


    # register requests exceptions
    app.register_error_handler(RequestException, requests_generic_error_handler)