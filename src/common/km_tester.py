"""
Python representation of a km_tester for
testing Kinetics models in System Biology
"""
import unittest  # for test cases
from src.common import simple_sbml
from src.common.simple_sbml import SimpleSBML


class KMTester(unittest.TestCase):

    def __init__(self, model_reference):
        """
        Initializes instance variables
        :param model_reference: string or SBML file
        """
        super().__init__()
        self.SBML = SimpleSBML(model_reference)

    def testParameterValueSet(self):
        """
        Checks whether the parameter values have been initialized
        Parameter values are considered unset if a model does not contain
        a setting for the "value" attribute of a parameter, nor does it has
        a default value
        :return: True iff all of the parameters have been initialized
        """
        for parameter in self.SBML.parameters:
            if not parameter.isSetValue():
                return False
        return True

    def testReactionChains(self):
        """
        Checks whether the reaction chains are valid
        :return:
        """
        # TODO: Implement testReactions