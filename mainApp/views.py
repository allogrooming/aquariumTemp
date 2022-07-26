from django.shortcuts import render
from django.views import generic

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializes import MemberTestSerializer
from .models import MemberTest


def test(request):
    test_object = MemberTest.objects.all()
    return render(request, 'test.html', {'test_object' : test_object})


class MemberList(APIView):

    # 가입자 명단 보여줌
    def get(self, request):
        members = MemberTest.objects.all()
        serializer = MemberTestSerializer(members, many=True)
        print("serializer data")
        print(serializer.data)
        return Response(serializer.data)

    # 회원가입
    def post(self, request):
        serializer = MemberTestSerializer(
            data = request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberTestDetail(APIView):
    
    # MemberTest 객체를 가져옴
    def get_object(self, pk):
        try:
            return MemberTest.objects.get(pk=pk)
        except MemberTest.DoesNotExist:
            raise Http404

    # MemberTest의 내용을 보여줌
    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberTestSerializer(member)
        return Response(serializer.data)

    # Member 정보 수정
    def put(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberTestSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Member 삭제
    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)