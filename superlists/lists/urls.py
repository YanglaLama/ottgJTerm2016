from django.conf.urls import include, url
from lists import views

urlpatterns = [
    # url(r'admin/', include(admin.site.urls))

    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),

]
