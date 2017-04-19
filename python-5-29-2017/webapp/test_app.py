#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import requests

payload = {"name": 1}
r = requests.post("http://127.0.0.1:5000/names/", json=payload)
r.text
