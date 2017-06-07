from django.test import TestCase
from angular4django.robot import robot
from rest_framework.test import APIClient

class RobotTestCase(TestCase):
    TEST_1 = """46B E59  EA C1F 45E  63
899 FFF 926 7AD C4E FFF
E2E 323 6D2 976 83F C96
9E9 A8B 9C1 461 F74 D05
EDD E94 5F4 D1D D03 DE3
 89 925 CF9 CA0 F18 4D2"""

    RESULT_1 = "r,r,d,d,r,d,d,r,r,d"

    TEST_4 = """46B E59  EA C1F 45E  63
899 FFF 926 7AD C4E FFF
E2E 323 6D2 976 83F C96
9E9 A8B 9CH 461 F74 D05
EDD E94 5F4 D1D D03 DE3
 89 925 CF9 CA0 F18 4D2"""


    def setUp(self):
        pass

    def test_supplied_test_case(self):
        """Verify the simple supplied test case"""
        client = APIClient()        
        response = client.post('/api/robot/', {'terrain': RobotTestCase.TEST_1}, format='json')
        import ipdb; ipdb.set_trace()
        self.assertEquals(response.data['result'], RobotTestCase.RESULT_1)

    def test_returns_error(self):
        """Verify the api returns an appropriate error"""
        client = APIClient()        
        response = client.post('/api/robot/', {'terrain': RobotTestCase.TEST_4}, format='json')
        self.assertTrue('9CH' in response.data['error'])