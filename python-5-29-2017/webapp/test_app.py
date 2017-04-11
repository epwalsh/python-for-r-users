#!/usr/bin/env python
# =============================================================================
# File Name:     test_app.py
# Author:        Evan Pete Walsh
# Contact:       epwalsh10@gmail.com
# Creation Date: 2017-04-11
# Last Modified: 2017-04-11 17:41:08
# =============================================================================

import requests

payload = {"name": 1}
r = requests.post("http://127.0.0.1:5000/names/", json=payload)
r.text
