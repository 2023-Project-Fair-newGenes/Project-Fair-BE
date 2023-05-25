from django.urls import path

from web.views import Test, Result, Upload, RequestInfo

urlpatterns = [
    path('test', Test.as_view(), name='test'),
    path('result', Result.as_view(), name='result'),
    path('upload', Upload.as_view(), name='upload'),
    path('requestInfo', RequestInfo.as_view(), name='requestInfo')
]