from rest_framework.views import APIView
from rest_framework.response import Response


class GetProfileView(APIView):
    def get(self, request):
        output = {
            "name": "MR BackEnd",
        }

        return Response(output)
    