from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name="landing"),
    path('password_reset/<uidb64>/<token>/', views.UserResetConfirm.as_view(), name='password_reset_confirm'),
]

htmx_urlpatterns = [
    path('journeys_count/', views.journeys_count, name="journeys_count"),
    path('journeys/', views.journeys, name="journeys"),
    path('journeys_count/', views.journeys_count, name="journeys_count"),
    path('signup/', views.UserCreate.as_view(), name="signup"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('nickname/<pk>/', views.UserNickname.as_view(), name="nickname"),
    path('get_logout/', views.get_logout, name="get_logout"),
    path('logout/', views.UserLogout.as_view(), name="logout"),
    path('password_reset/', views.UserReset.as_view(), name='password_reset'),
    path('start/', views.CreateJourney.as_view(), name="start"),
    path('journey/<slug:slug>/', views.JourneyDetail.as_view(), name="journey_detail"),
    path('journey/<slug:slug>/respond/', views.CreateResponse.as_view(), name="journey_respond")

]

urlpatterns += htmx_urlpatterns
