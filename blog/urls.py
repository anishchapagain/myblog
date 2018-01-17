from django.conf.urls import url
from blog.views import home, blog_add, blog_detail, blog_edit, blog_delete

urlpatterns = [
    url(r'^home/', home, name="home"),
    url(r'^add/', blog_add, name="blog_add"),
    url(r'^detail/(?P<blog_id>[0-9]+)', blog_detail, name="blog_detail"),
    url(r'^edit/(?P<blog_id>[0-9]+)', blog_edit, name="blog_edit"),
    url(r'^delete/(?P<blog_id>[0-9]+)', blog_delete, name="blog_delete"),
]