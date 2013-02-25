from django.conf.urls import patterns, include, url
from teachers import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.search, name='index'),
    url(r'^home/(?P<dbn>\w+)$', views.school, name='school'),
    url(r'^home/(?P<dbn>\w+)/(?P<teacher_id>\d+)$', views.teacher, name='teacher'),
    url(r'^load/', views.load),
    url(r'^drop/', views.drop),   
    url(r'^metatest/', views.metatest), 
    url(r'^search/$', views.search),    
    
    # url(r'^nycteacher/', include('nycteacher.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
