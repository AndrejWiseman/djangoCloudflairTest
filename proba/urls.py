from django.urls import path, include
from .views import index

from django_distill import distill_path


urlpatterns = [

    distill_path('',
                    index,
                    name='index',
                    # / is not a valid file name! override it to index.html
                    distill_file='index.html'),
]
