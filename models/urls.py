from django.urls import path
from . import views

urlpatterns = [

    path("all_models/", views.all_models),
    path("all_models/<int:id>/", views.all_models),
    path("all_brands/<int:id>/update/", views.put_update_shows),
    path('all_brands/<int:id>/add/', views.add_comment),

]