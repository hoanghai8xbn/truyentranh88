from django.urls import path
from .views import *
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register", register_user, name="register"),
    path("login/", views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path("profile/", profile_user, name="profile"),
    path("password_reset/", views.PasswordResetView.as_view(template_name="user/password_reset.html"),name="password_reset"),
    path("password_reset/done/", views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>", views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),name="password_reset_confirm"),
    path("password_reset_complete/", views.PasswordResetCompleteView.as_view(template_name="user/password_reset_confirm.html"),name="password_reset_complete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
