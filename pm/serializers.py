from rest_framework import serializers
from .models import User, Goods, OrderDetail

# 회원가입 API
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'userName', 'userPwd']  # 필드명 수정

# 제품 관련 API (등록/제거/조회/갱신)
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

# 주문등록 API
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'