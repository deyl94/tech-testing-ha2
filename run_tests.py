#!/usr/bin/env python2

import sys
import unittest
from tests.test_target_mail import SelectionOptionsTestCase, SaveTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(SelectionOptionsTestCase),
        unittest.makeSuite(SaveTestCase),
    ))i
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
