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


"""REST namespace Controller

Responses List :
    1xx -> :            Informational response - The request was received, continuing process
        * 100           Continue
        * 101           Switching Protocols
        * 102           Processing
        * 103           Early Hints (RFC 8297)

    2xx -> :            Successful - The request was successfully received, understood, and accepted
        * 200           Ok
        * 201           Created
        * 202           Accepted
        * 203           Non-Authoritative Information
        * 204           No Content
        * 205           Reset Content
        * 206           Partial Content
        * 207           Multi-Status
        * 208           Already Reported
        * 226           IM Used

    3xx -> :            Redirection - Further action needs to be taken in order to complete the request
        * 300           Multiple Choices
        * 301           Moved Permanently
        * 302           Found (Previously "Moved temporarily")
        * 303           See Other
        * 304           Not Modified
        * 305           Use Proxy
        * 306           Switch Proxy
        * 307           Temporary Redirect
        * 308           Permanent Redirect

    4xx -> :            Client Error - The request contains bad syntax or cannot be fulfilled
        * 400           Bad  Request
        * 401           Unauthorized
        * 402           Payment Required
        * 403           Forbidden
        * 404           Not Found
        * 405           Method Not Allowed
        * 406           Not Acceptable
        * 407           Proxy Authentication Required
        * 408           Request Timeout
        * 409           Conflict
        * 410           Gone
        * 411           Length Required
        * 412           Precondition Failed
        * 413           Payload Too Large
        * 414           URI Too Long
        * 415           Unsupported Media Type
        * 416           Range Not Satisfiable
        * 417           Expection Failed
        * 418           I'm a teapot
        * 421           Misdirected Request
        * 422           Unprocessable Entity
        * 423           Locked
        * 424           Failed Dependency
        * 425           Too Early
        * 426           Upgrade Required
        * 428           Precondition Required
        * 429           Too Many Requests
        * 431           Request Header Fields Too Large
        * 451           Unavailable For Legal Reasons

    5xx -> :            Server Error - The server failed to fulfil an apparently valid request
        * 500           Internal Server Error
        * 501           Not Implemented
        * 502           Bad Gateway
        * 503           Service Unavaliable
        * 504           Gateway Timeout
        * 505           HTTP Version Not Supported
        * 506           Variant Also Negotiates
        * 507           Insufficent Storage
        * 508           Loop Detected
        * 510           Not Extended
        * 511           Network Authentication Required


Functions:
    * get - returns list of datas
    * post - returns creation status with the newly created resource link
    * put - return update status with the the newly updated resource link
    * patch - returns the semi updated status with the newly semi updated resource link
    * delete - return delation status

"""


from flask_restplus import Resource
from flask import request, jsonify, make_response

from cart.dto.item_dto import ItemDto
from cart.repository.cart import Cart
from cart.repository.embed import Descriptions, Details, Items, Names
from cart.exception import ValueEmpty, DocumentDoesNotExist
from cart.blueprint.v1.item import namespace
from cart.middleware.jwt_auth_middleware import JWTAuthMiddleWare

@namespace.route('')
class CartItemsResource(Resource):
    def post(self):
        """Save data/datas to database

        ...

        Returns
        -------
            Json Dictionaries

        """
        ## Add an item to the cart
        jwtAuthMiddleWare = JWTAuthMiddleWare(request)
        auth = jwtAuthMiddleWare.authorize()
        # If auth is false break and return response to client
        # Else jwtAuthMiddleWare holds decoded users data
        if not auth:
            return jwtAuthMiddleWare.response

        ## TODO: Check if user have permission, or elese return 403 Forbidden
        
        if not namespace.payload["product_id"].strip() or \
           not namespace.payload["quantity"].strip():
           raise ValueEmpty({"payloads": namespace.payload})

        ## Either create new cart or update one
        cart = Cart.objects(customer_id = str(jwtAuthMiddleWare.user["data"]["id"]))

        item = Items(
            product_id = str(namespace.payload["product_id"]),
            quantity = int(namespace.payload["quantity"])
        )

        if not cart:
            ## Create new cart document
            new_cart = Cart(
                customer_id = str(jwtAuthMiddleWare.user["data"]["id"]),
                status = Cart.ACTIVE,
                items = [item]
            )
            new_cart.save()
            message = "Cart was not found for the user so new cart is created"
        else:
            old_cart = Cart.objects(customer_id = str(jwtAuthMiddleWare.user["data"]["id"])).get()
   
            old_cart.items.append(item)
            old_cart.save()
            message = "Item added to cart"

        return make_response(jsonify({
            "status_code": "201",
            "status": "Created",
            "message": message
        }))


@namespace.route('/<string:id>')
class CartItemResource(Resource):
    def delete(self, id):
        # start by validating request fields for extra security
        # step 1 validation: strip payloads for empty string
        if not id.strip():
           raise ValueEmpty({'payloads': {'id': id}})

        ## Add an item to the cart
        jwtAuthMiddleWare = JWTAuthMiddleWare(request)
        auth = jwtAuthMiddleWare.authorize()
        # If auth is false break and return response to client
        # Else jwtAuthMiddleWare holds decoded users data
        if not auth:
            return jwtAuthMiddleWare.response

        cart = Cart.objects(customer_id = jwtAuthMiddleWare.user["data"]["id"])
        cart.update(pull__items__id = Items(product_id = id).id)

        return make_response(jsonify({
            "status_code": 200,
            "status": "OK"
        }), 200)