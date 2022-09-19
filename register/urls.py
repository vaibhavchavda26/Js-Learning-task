from django.urls import path
from register import views


urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("register/<id>/", views.RegisterData.as_view(),name="registerdata")
]