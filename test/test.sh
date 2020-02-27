#!/bin/bash

TESTDIR=test


conda activate sklearn-tda
cd .. && pip install . && cd $TEST
python kmapper_to_mappercomplex_test.py

