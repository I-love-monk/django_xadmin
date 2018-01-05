# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.conf.urls import url, include

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MymessageView


urlpatterns = [
    #鐢ㄦ埛淇℃伅
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    #鐢ㄦ埛澶村儚涓婁紶
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    #鐢ㄦ埛涓汉涓績淇敼瀵嗙爜
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    #鍙戦�侀偖绠遍獙璇佺爜
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    #淇敼閭
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    #鎴戠殑璇剧▼
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    #鎴戞敹钘忕殑璇剧▼鏈烘瀯
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

    #鎴戞敹钘忕殑鎺堣璁插笀
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    #鎴戞敹钘忕殑璇剧▼
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    #鎴戠殑娑堟伅
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),
]