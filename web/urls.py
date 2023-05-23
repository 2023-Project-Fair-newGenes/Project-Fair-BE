from django.urls import path

from web.views import Test

urlpatterns = [
    path('test', Test.as_view(), name='test'),
]