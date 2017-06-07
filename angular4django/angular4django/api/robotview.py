from angular4django.robot import robot

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

class RobotView(APIView):
    """
    A simple APIView for getting robot paths
    """
    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        r = robot()
        try:
            r.parse_terrain(request.data['terrain'])
        except ValueError as e:
            return Response( { 'error': str(e)})

        r.walk(0,0)
        
        return Response({ 'result': r.result })

    def get(self, request, format=None):
        return Response('abc')