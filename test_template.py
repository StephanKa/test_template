# -*- coding: utf-8 -*-
""" DESCRIPTIONS HERE

"""
##############################################################################
# TODO:
#
# command line call:    python test_template.py <Test_Case_Name>[.<Test_Method>] [<Test_Case_Name>.<Test_Method>]...
# Test_Case_Name:       class name
# Test_method:          optional argument
# Example:              python test_template.py TestTemplateClass.test_xxx

import time
import unittest
import sys

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
    #
    # TODO: 
    # - test environment for multiple suites
    if __name__ == '__main__':
        begin_time = time.time()
        suite = unittest.TestSuite()
        if(len(sys.argv)) < 2:
            raise Exception('ERROR: A command-line parameter is missing')
        else:
            while(len(sys.argv) > 1):
                tmp_argument = sys.argv.pop(1)
                if(tmp_argument[0:2] == '--'):
                    # add optional parameter here
                    pass
                else:
                    # split the test method from test class
                    test_argument = tmp_argument.split('.')
                    if(len(test_argument) == 2):
                        test_case = test_argument[0]
                        test_method = test_argument[1]
                        suite.addTest((eval(test_case))(test_method))
                    elif(len(test_argument) == 1):
                        test_case = test_argument[0]
                        if(suite!=unittest.TestSuite()):
                            raise Exception('ERROR: Cannot have multiple test suites!')
                        suite = unittest.TestLoader().loadTestsFromTestCase(eval(test_case))
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
            
            runner = unittest.TextTestRunner(descriptions=False, verbosity = 2)
            test_res = runner.run(suite)
            print('Time elapsed: {0}sec'.format(time.time - begin_time))
            # check for errors or failures and return 0 or 1
            if((test_res.errors != []) or (test_res.failures != [])):
                sys.exit(1)
            else:
                sys.exit(0)
