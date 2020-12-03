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

from .details import Details

class Items(db.EmbeddedDocument):
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

    def non_zero_quantity(self, quantity):
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

    ## Fields
    product_id = db.StringField(required = True)

    quantity = db.IntField(default = 1)#, validation = non_zero_quantity)

    #details = db.DictField(db.EmbeddedDocumentField(Details))