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
from cart.repository.cart import Cart


class TestItemsapi():

    # consts
    STATUS_CHOICES = (
        Cart.ACTIVE,
        Cart.PENDING,
        Cart.COMPLETE,
        Cart.EXPIRING,
        Cart.EXPIRED
    )

    AM_WORD_LIST = (
        'አልማዝን', 'አየኋት', 'ከፈትኩላት', 'በሩን', 'ዘጋሁባት',
        'አየሩ', 'ተኝቷል', 'ኢትዮጵያ', 'ውስጥ', 'ናት', 'ከተማ'
    )

    def setup_class(self):
        # init faker object
        self.faker = Faker()
        # creating a FlaskClient instance to interact with the app
        self.app = create_app().test_client()


    def test_items_get_api(self):
        customer_id = self.faker.bothify('??#%??#%##?#?%###?%')
        url = '/api/v1/carts/%s/items' % customer_id
        # calling api endpoint
        items = self.app.get(url)
        # asserting status code
        assert items.status_code == 405


    def test_items_post_api(self):
        data = {
            'id': self.faker.bothify('??#%??'),
            'quantity': self.faker.bothify('%#'),
            'status': self.faker.sentence(ext_word_list = self.STATUS_CHOICES),
            'names': {
                'en': self.faker.sentence(),
                'am': self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
            },
            'descriptions': {
                'en': self.faker.sentence(),
                'am': self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
            }
        }
        customer_id = self.faker.bothify('??#%??#%##?#?%###?%')
        url = '/api/v1/carts/%s/items' % customer_id
        # calling apis endpoint
        items = self.app.post(url, json=data)
        #print(items.data)
        # asserting status code
        assert items.status_code == 201
         