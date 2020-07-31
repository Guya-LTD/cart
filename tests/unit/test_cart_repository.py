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

from cart.repository.cart import Cart

faker = Faker()

AM_WORD_LIST = (
    'አልማዝን', 'አየኋት', 'ከፈትኩላት', 'በሩን', 'ዘጋሁባት',
    'አየሩ', 'ተኝቷል', 'ኢትዮጵያ', 'ውስጥ', 'ናት', 'ከተማ'
)

STATUS_CHOICES = (
    Cart.ACTIVE,
    Cart.PENDING,
    Cart.COMPLETE,
    Cart.EXPIRING,
    Cart.EXPIRED
)

# list of carts
item_one = {
    'id': self.faker.bothify('??#%??#%##?#?%#'),
    'quantity': self.faker.bothify('%#'),
    'details': {
        'name': {
            'en': self.faker.sentence(),
            'am': self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
        },
        'description': {
            'en': self.faker.paragraph(),
            'am': self.faker.paragraph(ext_word_list = self.AM_WORD_LIST)
        }
    }
}

customer_id = faker.bothify('??#%??#%##?#?%###?%')
status = faker.sentence(ext_word_list = STATUS_CHOICES)

def test_object_creation(self):
    # cart object
    cart = Cart(
        customer_id = customer_id,
        status = status,
        items = [item_one]
    )
    
    isinstance(cart, Cart)

def test_object_creation_value_for_customer_id():
    assert cart.customer_id == customer_id

def test_object_creation_value_for_status():
    assert cart.status == status

def test_object_creation_value_for_item_one():
    assert cart.items[0] == item_one
