from django.urls import path, include
from authentication import views
from .views import ProfilePage


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    # path('profile/', ProfilePage.as_view(), name="profile"),
    # path('profile/<str:data>/', ProfilePage.as_view(), name="profile"),
    path('orders/', views.orders, name='orders'),
]
