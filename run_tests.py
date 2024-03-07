import unittest
import os
import xmlrunner
import sys

def run_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.getcwd(), 'Tests')

    suite = loader.discover(start_dir, pattern='test_')

    with open('test_results.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output, descriptions=True)
        result = runner.run(suite)

    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    exit_code = 0 if success else 1
    sys.exit(exit_code)
