from django.contrib import admin
from django.urls import path
from User import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, views as auth_views
from User.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostAddShowView.as_view(), name='addPost'),
    path('<int:id>/', views.PostUpdateView.as_view(), name="updatedata"),
    path('delete/<int:id>/', views.PostDeleteView.as_view(), name="deletedata"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',
    authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),




]
