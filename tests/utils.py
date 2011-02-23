#!/usr/bin/env python
"""Utilities for testing."""

import logging
import diffpy.srfit.equation.literals as literals

# Resolve the TestCaseSaSOptional class
try:
    import sans.pr.invertor
    import sans.models
    from unittest import TestCase as TestCaseSaSOptional
except ImportError, e:
    TestCaseSaSOptional = object
    logging.warning('%s, SaS tests skipped.', e)


def _makeArgs(num):
    args = []
    for i in xrange(num):
        j=i+1
        args.append(literals.Argument(name="v%i"%j, value=j))
    return args
