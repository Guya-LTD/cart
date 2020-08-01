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
from .embed.items import Items
from .mixins.timestamp_mixin import TimestampMixin
from cart.model.cart import Cart as CartEntity


class Cart(db.Document, CartEntity, TimestampMixin):
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

    ACTIVE: String
        default value = active

    PENDING: String
        default value = pending

    COMPLETE: String
        default value = complete

    EXPIRING: String
        default value = expiring

    EXPIRED: String
        default value = expired
    """
    
    ACTIVE = 'active'

    # checkout flow
    PENDING = 'pending'

    COMPLETE = 'complete'

    # cart expiration flow
    EXPIRING = 'expiring'

    EXPIRED = 'expired'

    STATUS_CHOICES = (
        ACTIVE,
        PENDING,
        COMPLETE,
        EXPIRING,
        EXPIRED
    )

    status = db.StringField(required = True, default = ACTIVE, choices = STATUS_CHOICES )

    customer_id = db.StringField(required = True)

    items = db.EmbeddedDocumentListField(Items)