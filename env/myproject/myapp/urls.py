
from django.conf.urls import url
from . import views

urlpatterns=[ url(r'^$',views.index,name='index'),
              url(r'^enquiry',views.enquiry,name='enquiry'),
              url(r'^new',views.new,name='new'),
              url(r'^delete/(?P<id>\d+) $',views.delete,name='delete'),
              url(r'^update/(?P<id>\d+)$',views.update,name='update'),
              url(r'^updateenq',views.updateenq,name='updateenq'),
              url(r'^upload', views.upload, name='upload'),
    ]
