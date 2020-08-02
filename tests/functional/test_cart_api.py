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
    flask-mongoengine v0.7

A pytest unit testing module.
"""

import pytest
import json
from faker import Faker

from cart import create_app

class TestCartApi():

    def setup_class(self):
        # init faker object
        self.faker = Faker()
        # creating a FlaskClient instance to interact with the app
        self.app = create_app().test_client()


    def test_carts_get_api(self):
        # calling apis endpoint
        carts = self.app.get('/api/v1/carts')
        #asserting status code
        assert carts.status_code == 405


    def test_carts_post_api(self):
        # calling apis endpoint
        carts = self.app.post('/api/v1/carts')
        # asserting status code
        assert carts.status_code == 405


    def test_cart_get_api_with_no_recored_id(self):
        id = self.faker.bothify('??#%??#%##?#?%###?%')
        # calling apis endpoint
        cart = self.app.get('/api/v1/carts/' + id)
        # asserting status code
        assert cart.status_code == 204


    def test_cart_get_api_with_recored_id(self):
        pass 


    def test_cart_get_api_with_empty_id(self):
        id = ' '
        # calling apis endpoint
        cart = self.app.get('/api/v1/carts/' + id)
        # asserting status code
        assert cart.status_code == 400


    def test_cart_put_api(self):
        id = self.faker.bothify('??#%??#%##?#?%###?%')
        # calling apis endpoint
        cart = self.app.put('/api/v1/carts/' + id)
        # asserting status code
        assert cart.status_code == 405


    def test_cart_delete_api_with_empty_id(self):
        id = ' '
        # calling apis endpoint
        cart = self.app.delete('/api/v1/carts/' + id)
        # asserting status code
        assert cart.status_code == 400

    
    def test_cart_delete_api_with_invalid_id(self):
        id = self.faker.bothify('??#%??#%##?#?%###?%')
        # calling apis endpoint
        cart = self.app.delete('/api/v1/carts/' + id)
        #body = json.loads(str(cart.data, 'utf8'))
        # asserting status code
        assert cart.status_code == 204
        #assert body['message']['description'] == 'Document not found from collection'
    

