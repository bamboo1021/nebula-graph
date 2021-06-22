# -*- coding: utf-8 -*-

# Copyright (c) 2020 vesoft inc. All rights reserved.
#
# This source code is licensed under Apache 2.0 License,
# attached with Common Clause Condition 1.0, found in the LICENSES directory.


import sys

import pytest
from pytest_bdd import scenarios

scenarios('features', 'openCypher/features')
caller = sys._getframe(0).f_locals
frame_keys = caller.copy().keys()

record_list = []

for item in frame_keys:
    if item.startswith('test'):
        r = {}
        func = caller[item]
        r['feature'], r['scenario'] = func.__doc__.split(':', 1)
        r['feature'], r['scenario'] = r['feature'].strip(), r['scenario'].strip()
        r['steps'] = len(func.__scenario__.steps)
        record_list.append(r)

with open('count_tck.csv', 'w') as fl:
    fl.write('feature|scenario|steps\n')
    for r in record_list:
        fl.write('{}|{}|{}'.format(r['feature'], r['scenario'], r['steps']))
        fl.write('\n')
    fl.flush()

