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

from .names import Names
from .descriptions import Descriptions

class Details(db.EmbeddedDocument):
    """Embedded document.
    
    Attributes
    ----------
    names: dict
        EN and AM language names
        
    descriptions:
        EN and AM language descriptions
    """

    names = db.DictField(db.EmbeddedDocumentField(Names))

    descriptions = db.DictField(db.EmbeddedDocumentField(Descriptions))