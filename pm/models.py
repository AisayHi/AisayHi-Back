from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# UserManager 클래스: 사용자 생성 및 슈퍼유저 생성을 위한 메서드 정의
class UserManager(BaseUserManager):
    def create_user(self, userId, userName, userPwd, **extra_fields):
        if not userId:
            raise ValueError('The userId must be set')
        user = self.model(userId=userId, userName=userName, **extra_fields)
        user.userPwd = make_password(userPwd)
        user.save(using=self._db)
        return user

    def create_superuser(self, userId, userName, userPwd, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(userId, userName, userPwd, **extra_fields)


# User 클래스: 사용자 모델 정의
class User(AbstractBaseUser, PermissionsMixin):
    userKey = models.AutoField(primary_key=True)  # 사용자 고유번호
    userId = models.CharField(unique=True, max_length=50)  # 사용자 아이디
    userName = models.CharField(max_length=20)  # 사용자 이름
    userPwd = models.CharField(max_length=128)  # 비밀번호

    # 필수 필드들
    is_staff = models.BooleanField(default=False)  # 직원 여부 필드
    is_active = models.BooleanField(default=True)  # 활성 사용자 여부 필드
    date_joined = models.DateTimeField(default=timezone.now)  # 가입 날짜 필드

    # groups 및 user_permissions의 related_name 추가
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # 충돌 방지
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # 충돌 방지
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user_permissions'
    )

    USERNAME_FIELD = 'userId'  # 사용자 모델에서 유일한 식별자로 사용할 필드
    REQUIRED_FIELDS = ['userName']  # 사용자 생성 시 반드시 필요한 필드

    objects = UserManager()  # UserManager를 사용자 모델의 매니저로 설정

    class Meta:
        db_table = 'pm_user'


# SituationCategory 테이블에 맞는 모델
class SituationCategory(models.Model):
    situationCateKey = models.AutoField(primary_key=True)  # 카테고리 고유번호
    situationCategory1 = models.CharField(max_length=30)  # 1차 카테고리명
    situationCategory2 = models.CharField(max_length=30)  # 2차 카테고리명
    situationCategory3 = models.CharField(max_length=30)  # 3차 카테고리명

    class Meta:
        db_table = 'situationCategory'


# Situation 테이블에 맞는 모델
class Situation(models.Model):
    situationKey = models.AutoField(primary_key=True)  # 상황 고유번호
    situationCateKey = models.ForeignKey(SituationCategory, on_delete=models.CASCADE)  # 카테고리 외래키
    headline1 = models.CharField(max_length=50, blank=True, null=True)  # 상황 문구
    headline2 = models.CharField(max_length=50, blank=True, null=True)  # 상황 문구 부제
    mainKeyword = models.CharField(max_length=30, blank=True, null=True)  # 강조 단어

    class Meta:
        db_table = 'situation'


# SituationKeyword 테이블에 맞는 모델
class SituationKeyword(models.Model):
    situationKwKey = models.AutoField(primary_key=True)  # 상황 키워드 고유번호
    situationKey = models.ForeignKey(Situation, on_delete=models.CASCADE)  # 상황 고유번호
    situationKeyword = models.CharField(max_length=30)  # 상황 키워드

    class Meta:
        db_table = 'situationKeyword'


# GoodsCategory 테이블에 맞는 모델
class GoodsCategory(models.Model):
    goodsCateKey = models.AutoField(primary_key=True)  # 상품 카테고리 고유번호
    categoryName = models.CharField(max_length=50)  # 카테고리명

    class Meta:
        db_table = 'goodsCategory'


# Goods 테이블에 맞는 모델
class Goods(models.Model):
    goodsKey = models.AutoField(primary_key=True)  # 상품 고유번호
    goodsCateKey = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE)  # 상품 카테고리 외래 키
    ASIN = models.CharField(max_length=30)  # 아마존 표준 식별 번호
    goodsName = models.CharField(max_length=30)  # 상품명
    brand = models.CharField(max_length=30, blank=True, null=True)  # 브랜드
    originalPrice = models.IntegerField()  # 정가
    discountedPrice = models.IntegerField()  # 할인가
    ratingAvg = models.FloatField(blank=True, null=True)  # 평균 별점
    ratingCount = models.IntegerField(blank=True, null=True)  # 별점 개수
    goodsInfo = models.CharField(max_length=150, blank=True, null=True)  # 상품 특징
    goodsDesc = models.CharField(max_length=150, blank=True, null=True)  # 상품 정보

    class Meta:
        db_table = 'goods'


# Orders 테이블에 맞는 모델
class Orders(models.Model):
    orderKey = models.AutoField(primary_key=True)  # 주문 번호
    userKey = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 외래 키
    totalPrice = models.IntegerField()  # 총 결제 금액
    rdate = models.DateField()  # 주문 날짜

    class Meta:
        db_table = 'orders'


# OrderDetail 테이블에 맞는 모델
class OrderDetail(models.Model):
    orderDetKey = models.AutoField(primary_key=True)  # 주문 상세 고유번호
    orderKey = models.ForeignKey(Orders, on_delete=models.CASCADE)  # 주문 외래 키
    goodsKey = models.ForeignKey(Goods, on_delete=models.CASCADE)  # 상품 외래 키
    price = models.IntegerField()  # 가격
    cnt = models.IntegerField()  # 개수

    class Meta:
        db_table = 'orderDetail'
