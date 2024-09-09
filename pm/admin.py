from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Goods, Orders, Situation, User, OrderDetail

# CustomUserAdmin 클래스 정의
class CustomUserAdmin(BaseUserAdmin):
    model = User

    fieldsets = (
        (None, {'fields': ('userId', 'userName', 'password')}),
        (_('Personal info'), {'fields': ('date_joined', 'last_login')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('userId', 'userName', 'password1', 'password2'),
        }),
    )

    list_display = ('userId', 'userName', 'is_staff', 'is_superuser')  # 관리 화면에 표시할 필드
    search_fields = ('userId', 'userName')  # 검색 가능한 필드
    ordering = ('userId',)  # 정렬 필드

# 이미 등록된 User 모델이 있는지 확인하고 중복 등록을 방지
try:
    admin.site.register(User, CustomUserAdmin)
except admin.sites.AlreadyRegistered:
    pass

# 다른 모델 등록
admin.site.register(Goods)
admin.site.register(Orders)
admin.site.register(Situation)
admin.site.register(OrderDetail)
