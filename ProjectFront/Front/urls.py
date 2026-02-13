from django.urls import path
from hello import views


urlpatterns = [
    path('prime/', views.prime)
]
