# defaults.py
#
# Copyright (c) 2026 Markus Binsteiner
# All rights reserved.
#
# SPDX-License-Identifier: 0BSD
#
# Licensed under the BSD Zero Clause License

"""Filesystem locations for data bundled with the template_test package."""

import sys
from pathlib import Path

if hasattr(sys, "_MEIPASS"):
    # Running from a PyInstaller bundle: package data is unpacked under the
    # bundle's temp dir instead of living next to this file.
    PACKAGE_MODULE_BASE_FOLDER = Path(sys._MEIPASS) / "template_test"
else:
    PACKAGE_MODULE_BASE_FOLDER = Path(__file__).parent

RESOURCES_FOLDER = PACKAGE_MODULE_BASE_FOLDER / "resources"
