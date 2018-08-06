from django.db import models

"""定义UserInfo表"""


class UserInfo(models.Model):
    userName = models.CharField(max_length=20, unique=True, db_column="user_name")
    password = models.CharField(max_length=50)

    class Meta():
        db_table = 'user_userinfo'


"""定义UserContact表跟UserInfo表时一对一"""


class UserContact(models.Model):
    userInfo = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=50)