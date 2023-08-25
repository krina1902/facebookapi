from django.contrib import admin
from django.urls import path, include
# from core import views as core_views

from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', core_views.HomeView.as_view(), name='home'),

    # Login and Logout
    path('login/',views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('social-auth/', include('social_django.urls', namespace='social')), 
    path('',views.home,name='home'), # <-- here
]