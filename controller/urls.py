from django.urls import path
from controller import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.handlelogin,name="handlelogin"),
    path('logout/',views.handlelogout,name="handlelogout"),
    path('request-password-reset/', views.RequestPasswordResetView.as_view(), name='request-password-reset'),
    path('set-new-password/', views.SetNewPasswordView.as_view(), name='set_new_password'),
]
