from django.urls import path
from . import views
urlpatterns = [
    path('photos/upload',views.photoupload.as_view(),name='upload'),
    path("photos",views.photo.as_view(),name='display'),
    path('delete',views.delete.as_view(),name='delete_item'),
    
]
