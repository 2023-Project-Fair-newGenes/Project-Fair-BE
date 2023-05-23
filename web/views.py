from rest_framework.response import Response
from rest_framework.views import APIView


class Test(APIView):
    def get(self, request):
        return Response({
            "Response" : "success"
        })

class Result(APIView):
    def get(self, request):

        user_id = request.data.get('user_id')
        print(user_id)

        return Response({
            "Response" : "success"
        })