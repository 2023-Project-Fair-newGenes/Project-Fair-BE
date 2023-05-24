from django.urls import path

from web.views import Test, Result

urlpatterns = [
    path('test', Test.as_view(), name='test'),
    path('result', Result.as_view(), name='result'),
]