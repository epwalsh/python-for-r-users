#!/usr/bin/env python
# =============================================================================
# File Name:     foo.py
# Author:        Evan Pete Walsh
# Contact:       epwalsh10@gmail.com
# Creation Date: 2017-04-28
# Last Modified: 2017-04-28 21:44:10
# =============================================================================

"""
docstring
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pandas as pd

df = pd.read_csv('./data/flights.csv')

df.head()

df.groupby('carrier').agg({
    'dep_delay': {
        'mean': lambda x: x.mean()
    }
})
