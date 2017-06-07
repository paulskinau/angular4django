from django.test import TestCase
from angular4django.robot import robot


class RobotTestCase(TestCase):
    TEST_1 = """46B E59  EA C1F 45E  63
899 FFF 926 7AD C4E FFF
E2E 323 6D2 976 83F C96
9E9 A8B 9C1 461 F74 D05
EDD E94 5F4 D1D D03 DE3
 89 925 CF9 CA0 F18 4D2"""

    RESULT_1 = "r,r,d,d,r,d,d,r,r,d"

    TEST_2 = """0 0 0 0 0 0
0 FFF 926 7AD C4E 0
0 323 6D2 976 83F 0
0 A8B 9C1 461 F74 0
0 E94 5F4 D1D D03 0
0 0 0 0 0 0"""

    RESULT_2 = 'd,d,d,d,d,r,r,r,r,r'

    TEST_3 = """46B E59  EA C1F 45E  63
899 FFF 926 7AD C4E FFF
E2E 323 6D2 976 83F C96
9E9 A8B 9C1 F74 D05
EDD E94 5F4 D1D D03 DE3
 89 925 CF9 CA0 F18 4D2"""

    TEST_4 = """46B E59  EA C1F 45E  63
899 FFF 926 7AD C4E FFF
E2E 323 6D2 976 83F C96
9E9 A8B 9CH 461 F74 D05
EDD E94 5F4 D1D D03 DE3
 89 925 CF9 CA0 F18 4D2"""

    TEST_5 = ""
    RESULT_5 = ""

    def setUp(self):
        pass

    def test_supplied_test_case(self):
        """Verify the simple supplied test case"""
        r = robot()
        r.parse_terrain(RobotTestCase.TEST_1)
        r.walk(0,0)
        self.assertEquals(r.result, RobotTestCase.RESULT_1)

    def test_order_of_results(self):
        """Given two possible solutions, which one is returned?"""
        r = robot()
        r.parse_terrain(RobotTestCase.TEST_2)
        r.walk(0,0)
        self.assertEquals(r.result, RobotTestCase.RESULT_2)

    def test_row_missing_value(self):
        """One row is missing a value"""
        r = robot()
        with self.assertRaises(ValueError) as context:
            r.parse_terrain(RobotTestCase.TEST_3)

    def test_non_hex_value(self):
        """ one row has a non-hex value """
        r = robot()
        with self.assertRaises(ValueError) as context:
            r.parse_terrain(RobotTestCase.TEST_4)
    
    def test_empty_input(self):
        """ test absolutely no terrain """
        r = robot()
        with self.assertRaises(ValueError) as context:
            r.parse_terrain(RobotTestCase.TEST_5)