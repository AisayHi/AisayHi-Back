from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

# 사용자
from django.contrib.auth import authenticate, login
from .models import User

# 상품
from .models import Goods
from .serializers import GoodsSerializer

# 주문
from .models import OrderDetail
from .serializers import OrderDetailSerializer

# 회원가입 API: 아이디, 이름, 비밀번호
@csrf_exempt
def signup_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            userId = data.get('userId')  # login_id -> userId로 변경
            userName = data.get('userName')  # username -> userName으로 변경
            userPwd = data.get('userPwd')  # userpwd -> userPwd로 변경

            # 아이디, 사용자명, 비밀번호 중 하나라도 입력하지 않으면 -> 에러
            if not userId or not userName or not userPwd:
                return JsonResponse({'error': 'Missing fields'}, status=400)

            # 사용자가 이미 존재하는지 확인 -> 중복 회원가입 방지
            if User.objects.filter(userId=userId).exists():
                return JsonResponse({'error': 'User already exists'}, status=400)

            user = User(
                userId=userId,
                userName=userName,
                userPwd=userPwd
            )
            user.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)

# 로그인 API: 아이디, 비밀번호
@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            userId = data.get('userId')  # login_id -> userId로 변경
            userPwd = data.get('userPwd')  # userpwd -> userPwd로 변경

            if not userId or not userPwd:
                return JsonResponse({'error': 'Missing fields'}, status=400)

            # 사용자 인증 - 아이디, 비밀번호
            user = authenticate(request, userId=userId, password=userPwd)

            # 사용자가 존재한다면
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'message': 'Login successful',
                    'user': {
                        'userId': user.userId,  # login_id -> userId로 변경
                    },
                }, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)

# 제품 관련 API: 모든 필드 사용 (등록/제거/조회/갱신)
# -- 제품 데이터에 대한 CRUD 및 검색/필터링/정렬 기능 제공
class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # 필터링/검색/정렬 백엔드 설정
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 필터링 필드 설정: category와 brand 필드를 사용하여 필터링 가능
    filterset_fields = ['category', 'brand']

    # 검색 필드 설정: goodsName과 goodsDesc 필드를 사용하여 검색 가능
    search_fields = ['goodsName', 'goodsDesc']  # 필드명 수정

    # 정렬 필드 설정: price와 discountedPrice 필드를 사용하여 정렬 가능
    ordering_fields = ['price', 'discountedPrice']

# 주문 상세 API: 모든 필드 사용
class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()  # OrderDetail 모델의 모든 데이터를 가져옴
    serializer_class = OrderDetailSerializer