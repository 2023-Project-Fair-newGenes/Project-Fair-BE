from django.http import HttpResponseNotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage

import os

from web.detectionSNP import detection, getCharacteristic
from web.models import LifestyleInformation


class Test(APIView):
    def get(self, request):
        return Response({
            "Response" : "success"
        })

class Result(APIView):
    def get(self, request):

        user_id = request.query_params.get('user_id')

        csv_filename = user_id + ".csv"
        directory_name = 'genome_file'

        current_directory = os.getcwd()
        csv_path = os.path.join(current_directory, directory_name)
        csv_path = os.path.join(csv_path, csv_filename)

        if os.path.isfile(csv_path):
            find_snp_list = detection(csv_path)
            result = getCharacteristic(find_snp_list)
        else:
            error_message = "CSV 파일 " + csv_filename + "가 존재하지 않습니다."
            return HttpResponseNotFound(error_message)

        return Response(result)
        
class Upload(APIView):
    def post(self, request):
        user_id = request.data.get('user_id') #사용자 아이디 6자리
        genome_file = request.FILES.get('genome_file') #게놈 데이터 파일

        file_storage = FileSystemStorage()
        filename = file_storage.save("genome_file/" + user_id + ".csv", genome_file)

        if filename:
            print("사용자의 게놈 데이터가 저장되었습니다.")
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RequestInfo(APIView):
    def get(self, request):
        # rsid = request.data.get('id') #유전자 rsid
        rsid = request.query_params.get('id') #유전자 rsid
        info = LifestyleInformation.objects.filter(snp_id = rsid)

        lifestyle_info = []

        for _info in info:
            lifestyle_info.append(_info.info)

        result = {}
        result['id'] = rsid
        result['lifestyle_info'] = lifestyle_info

        return Response(result)