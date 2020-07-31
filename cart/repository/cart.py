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


flask-mongoengine based ODM flask-mongoengine built up on pymongo engine.
"""

from cart.database import db
from .mixins.timestamp_mixin import TimestampMixin
from cart.model.cart import Cart as CartEntity


class CartItems(db.EmbeddedDocument, TimestampMixin):
    """Embedded document.
    
    Attributes
    ----------
    id: String
        Products/Item id

    quantity: int
        Quantity of item

    details: dict
        The details field in each line item allows your application 
        to display the cart contents to the user without requiring 
        a second query to fetch details from the catalog collection.
    """

    id = db.StringField(required = True)

    quantity = db.IntField(default = 1, validation = self.non_zero_quantity)

    details = db.DictField()

    def non_zero_quantity(quantity):
        """A callable to validate the value of the field. 
        The callable takes the value as parameter and should 
        raise a ValidationError if validation fails

        Validates for non zero quantity i.e quantity must be atlist 1

        Parameters:
        ----------
        quantity: int
        """

        if quantity < 1:
            raise ValidationError('Quantity must be atlist one or greater than one')



class Cart(CartEntity):
    """Cart ODM
    ...
    
    Attributes
    ----------
    _id : String 
        Auto inherated attribute, 12-byte, 24 char hexadicmal

    status: String('active', 'inactive', 'pending', 'complete', 'expiring', 'expired')
        statue of the cart

    customer_id: String
        User's id

    items: array
        Cart times
    """

    STATUS_CHOICES = (
        self.ACTIVE,
        self.PENDING,
        self.COMPLETE,
        self.EXPIRING,
        self.EXPIRED
    )

    status = db.StringField(required = True, default = self.ACTIVE, choices = self.STATUS_CHOICES )

    customer_id = db.StringField(required = True)

    items = db.ListField(db.DictField(db.EmbeddedDocumentField(CartItems)))