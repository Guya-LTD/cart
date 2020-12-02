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


"""Logging handler."""

import os
import sys
import logging
import logstash


# const vars
__extra__ = {
    'app_name': 'Branch Service',      
    'environment': os.getenv('ENV'),  
    'container_host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
    'sys': {
        'lang': 'python',
        'version': str(sys.version),
        'version_info': repr(sys.version_info)
    }
}


# Logger with app name i.e xtrack.main
logger = logging.getLogger(__name__)


# logger handler
logger.addHandler(
    logstash.TCPLogstashHandler(
        #"logstash-logstash.guya-ltd-elk.svc.cluster.local",
        #5400, 
        os.getenv('LOGGING_HOST'),
        os.getenv('LOGGING_PORT'), 
        version=1
    )
)

def log_exception(error, extra) -> None:
    myextra = __extra__
    myextra.update(extra)
    # recommanded for production or eithre the logging servier is running
    logger.exception(str(error), extra = myextra)