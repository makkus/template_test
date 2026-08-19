# defaults.py
#
# Copyright (c) 2026 Markus Binsteiner
# All rights reserved.
#
# SPDX-License-Identifier: 0BSD
#
# Licensed under the BSD Zero Clause License

import os
import sys

if getattr(sys, "oxidized", False):
    PACKAGE_MODULE_BASE_FOLDER = "xxx"
    raise NotImplementedError()
elif not hasattr(sys, "_MEIPASS"):
    PACKAGE_MODULE_BASE_FOLDER = os.path.dirname(__file__)
else:
    PACKAGE_MODULE_BASE_FOLDER = os.path.join(sys._MEIPASS, "template_test")

RESOURCES_FOLDER = os.path.join(PACKAGE_MODULE_BASE_FOLDER, "resources")
