from django.urls import path, include

from . import views
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.homepage, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.homepage, name="dashboard"),

    path('chatpage', views.chatpage, name="chatpage"),

    path('home', views.home, name="home"),

    path('email', views.email_attatchment_send, name='email'),

    path('encode/', views.encode_view, name='encode'),

    path('decode/', views.decode_view, name='decode'),

    path("logout-user", views.logout_user, name="logout-user"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)