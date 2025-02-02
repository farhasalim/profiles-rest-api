from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path ('hello-view/', views.HelloApiView.as_view()),
    path ('', include(router.urls)) #As you register new routes with our router above, it generates 
    # a new list of urls associated for viewset. It will figure out URLs for all functions we add to our viewset
    # and then generates urls list which we can pass in with the path and include. 
    # Blank string = since we don't want to add a prefix to the URLS
]