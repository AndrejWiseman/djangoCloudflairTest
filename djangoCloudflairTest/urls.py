
from django.contrib import admin
from django.urls import path, include


from django_distill import distill_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proba.urls')),

    # distill_path('',
    #                 IndexView.as_view(),
    #                 name='index',
    #                 # / is not a valid file name! override it to index.html
    #                 distill_file='index.html'),
]
