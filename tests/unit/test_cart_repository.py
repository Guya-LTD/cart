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
from faker import Faker

from cart.repository.embed import Descriptions, Details, Items, Names
from cart.repository.cart import Cart

class TestCartRepository():

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
        # init cart object
        self.customer_id = self.faker.bothify('??#%??#%##?#?%###?%')
        self.status = self.faker.sentence(ext_word_list = self.STATUS_CHOICES)
        # list of carts
        self.name = Names(
            en = self.faker.sentence(),
            am = self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
        )
        self.description = Descriptions(
            en = self.faker.paragraph(),
            am = self.faker.paragraph(ext_word_list = self.AM_WORD_LIST)
        )
        self.detail = Details(
            names = self.name,
            descriptions = self.description
        )
        self.item = Items(
            id = self.faker.bothify('??#%??#%##?#?%#'),
            quantity = self.faker.bothify('%#'),
            details = self.detail
        )

        # cart
        self.cart = Cart(
            customer_id = self.customer_id,
            status = self.status,
            items = [self.item]
        )


    #def teardown_method(self):
        # destory cart object from memory
        #del self.cart


    def test_object_creation(self):
        isinstance(self.cart, Cart)


    def test_object_creation_value_for_customer_id(self):
        assert self.cart.customer_id == self.customer_id


    def test_object_creation_value_for_status(self):
        assert self.cart.status == self.status


    def test_object_creation_value_for_item_one(self):
        assert self.cart.items[0] == self.item