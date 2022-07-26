from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemberList, MemberTestDetail

urlpatterns = [
    path('member/', MemberList.as_view()),
    path('member/<int:pk>/', MemberTestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)