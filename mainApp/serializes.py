from rest_framework import serializers
from .models import MemberTest

class MemberTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTest
        fields = ('member_code', 'member_id', 'member_password', 'member_name',
        'member_nickname', 'member_email', 'member_gender', 'member_dob', 'member_join_date', 'member_pic')