from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), 
    path("new-reminder/", views.new_reminder),
    # This URL has been provided to help with the test (Do not change the URLs)
    path("<int:id>/delete", views.delete_reminder),
    path("math/", views.calculate, name='math')
]
