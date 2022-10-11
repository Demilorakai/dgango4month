from django.urls import path
from models import views
urlpatterns = [


    path("all_brands/", views.all_brands, name='all_brands'),
    path("all_brands/<int:id>/", views.all_models),

]