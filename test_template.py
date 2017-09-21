# -*- coding: utf-8 -*-
""" GENERAL TEST DESCRIPTION HERE

TODO: -

command line call:    python test_template.py <Test_Case_Name>[.<Test_Method>] [<Test_Case_Name>.<Test_Method>]...
Test_Case_Name:       class name
Test_method:          optional argument
Example:              python test_template.py TestTemplateClass.test_xxx
"""
import time
import unittest
import sys
import os
import xmlrunner


class TestTemplateClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_xxx(self):
        ''' DESCRIBE TEST HERE'''
        pass

if sys.version_info < (3, 0):
    # Note:
    # The loader that sorts the test by their order of definition doesn't
    # work on Python 3.
    if __name__ == '__main__':
        BEGIN_TIME = time.time()
        SUITE = unittest.TestSuite()
        if(len(sys.argv)) < 2:
            if(not os.path.exists('coverage')):
                os.mkdir('coverage')
            with open('coverage/test-results.xml', 'wb') as output:
                unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output),
                              # these make sure that some options that are not applicable
                              # remain hidden from the help menu.
                              failfast=False, buffer=False, catchbreak=False)
        else:
            while(len(sys.argv) > 1):
                TMP_ARGUMENT = sys.argv.pop(1)
                if(TMP_ARGUMENT[0:2] == '--'):
                    # add optional parameter here
                    pass
                else:
                    # split the test method from test class
                    TEST_ARGUMENT = TMP_ARGUMENT.split('.')
                    if(len(TEST_ARGUMENT) == 2):
                        TEST_CASE = TEST_ARGUMENT[0]
                        TEST_METHOD = TEST_ARGUMENT[1]
                        SUITE.addTest((eval(TEST_CASE))(TEST_METHOD))
                    elif(len(TEST_ARGUMENT) == 1):
                        TEST_CASE = TEST_ARGUMENT[0]
                        if(SUITE != unittest.TestSuite()):
                            raise Exception('ERROR: Cannot have multiple test suites!')
                        SUITE = unittest.TestLoader().loadTestsFromTestCase(eval(TEST_CASE))
                    else:
                        raise Exception('ERROR: invalid test case specification!')
            # set the test runner with parameters (description, verbosity, stream)
            # description means the test method description
            # verbosity is the output for the test suite
            # stream is a stream that can be output to other instances for example see code below:
            #
            # from StringIO import StringIO
            #
            # stream = StringIO()
            # runner = unittest.TextTestRunner(stream = stream)
            # print('Test Output\n{}'.format(stream.read()))
            RUNNER = unittest.TextTestRunner(descriptions=False, verbosity=2)
            TEST_RESULTAT = RUNNER.run(SUITE)
            print('Time elapsed: {0}sec'.format(time.time() - BEGIN_TIME))
            # check for errors or failures and return 0 or 1
            if((TEST_RESULTAT.errors != []) or (TEST_RESULTAT.failures != [])):
                sys.exit(1)
            else:
                sys.exit(0)
