"""
Tests for km_tester
"""

import unittest
from src.common.km_tester import KMTester
from tests.common import helpers


#############################
# Tests
#############################
class TestKMTester(unittest.TestCase):

    def setUp(self):
        self.KM = helpers.getKM()

    def testTestParameterValueSet(self):
        self.KM.testParameterValueSet()

    def testTestReactionChains(self):
        self.KM.testReactionChains()
