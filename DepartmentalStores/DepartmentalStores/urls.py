from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from stores import views, locationView, departmentView, categoryView, subCategoryView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('locations/', locationView.LocationPostAPIView.as_view()),
    re_path(r'^locations/(?P<pk>[0-9]+)/$', locationView.LocationRudView.as_view()),
    re_path(r'^locations/(?P<pk>[0-9]+)/departments/$', departmentView.DepartmentPostAPIView.as_view()),
    re_path(r'^locations/(?P<loc_id>[0-9]+)/departments/(?P<pk>[0-9]+)/$', departmentView.DepartmentRudView.as_view()),
    re_path(r'^locations/(?P<loc_id>[0-9]+)/departments/(?P<pk>[0-9]+)/categories/$', categoryView.CategoryPostAPIView.as_view()),
    re_path(r'^locations/(?P<loc_id>[0-9]+)/departments/(?P<dept_id>[0-9]+)/categories/(?P<pk>[0-9]+)/$', categoryView.CategoryRudView.as_view()),
    re_path(r'^locations/(?P<loc_id>[0-9]+)/departments/(?P<dept_id>[0-9]+)/categories/(?P<pk>[0-9]+)/subcategories/$', subCategoryView.SubCategoryPostAPIView.as_view()),
    re_path(r'^locations/(?P<loc_id>[0-9]+)/departments/(?P<dept_id>[0-9]+)/categories/(?P<cat_id>[0-9]+)/subcategories/(?P<pk>[0-9]+)/$', subCategoryView.SubCategoryRudView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)