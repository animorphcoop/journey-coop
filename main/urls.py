from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('signup/', views.UserCreate.as_view(), name="signup"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('nickname/<pk>/', views.UserNickname.as_view(), name="nickname"),
    path('logout/', views.UserLogout.as_view(), name="logout"),
    path('password_reset/', views.UserReset.as_view(), name='password_reset'),
    path('password_reset/<uidb64>/<token>/', views.UserResetConfirm.as_view(), name='password_reset_confirm'),
    path('start/', views.CreateJourney.as_view(), name="start"),
    path('journey/<slug:slug>/', views.JourneyDetail.as_view(), name="journey_detail"),
    path('journey/<slug:slug>/respond/', views.CreateResponse.as_view(), name="journey_respond")
]
