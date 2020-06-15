from django.urls import path
from . import views

#name represents the identifier for this view. whereas views.post_list is the name of the view file to be rendered.

urlpatterns = [
    path('', views.py, name='code_home'),
    path('start_vid', views.start_vid, name='start_vid'),
    path('stop_vid', views.stop_vid, name='stop_vid'),
    path('logs', views.logtable, name='logs'),
]