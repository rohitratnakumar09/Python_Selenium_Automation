import unittest
from tests.Login.Login_Tests import Login_Test
from tests.Login.Login_Test_CSV import Login_Test_CSV

# Get all tests from the test classes
# tc1 = unittest.TestLoader().loadTestsFromTestCase(Login_Test)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(Login_Test_CSV)
# Create a test suite combining all test classes
smokeTest = unittest.TestSuite()
smokeTest.addTest(unittest.makeSuite(Login_Test))
smokeTest.addTest(unittest.makeSuite(Login_Test_CSV))
#unittest.TextTestRunner(verbosity=2).run(smokeTest)



