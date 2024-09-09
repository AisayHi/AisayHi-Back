from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class orderDetail(models.Model):
    situation = models.ForeignKey('Situation', on_delete=models.CASCADE)
    detail_id = models.AutoField(primary_key=True)
    detail = models.CharField(max_length=150)

    class Meta:
        db_table = 'detail'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goodsname = models.CharField(db_column='goodsName', max_length=30)
    category = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    goodsdesc = models.CharField(db_column='goodsDesc', max_length=150, blank=True, null=True)
    goodsimg = models.TextField(db_column='goodsImg', blank=True, null=True)
    price = models.IntegerField()
    discountprice = models.IntegerField(db_column='discountPrice', blank=True, null=True)

    class Meta:
        db_table = 'goods'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    item_id = models.IntegerField()
    itemcnt = models.IntegerField(db_column='itemCnt')
    itemprice = models.IntegerField(db_column='itemPrice')
    totalprice = models.IntegerField(db_column='totalPrice')

    class Meta:
        db_table = 'orders'


class Situation(models.Model):
    situation_id = models.AutoField(primary_key=True)
    situationcategory = models.CharField(db_column='situationCategory', max_length=50)
    situation = models.CharField(max_length=30)
    keyword = models.CharField(max_length=30)
    headline = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'situation'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    login_id = models.CharField(unique=True, max_length=50)
    username = models.CharField(max_length=20)
    userpwd = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'
