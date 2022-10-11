from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from .views import  RegisterView, PasswordChangeView
from .views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(template_name="register.html"), name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change/', MyPasswordChangeView.as_view(),  name='change_password'),
    path('change_done/', MyPasswordResetDoneView.as_view(), name='change_done'),
    # path('change/', PasswordChangeView.as_view(template_name="registration/account.html"), name='change'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

