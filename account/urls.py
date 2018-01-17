from django.conf.urls import url
from account.views import  ( user_register, user_login, 
								user_logout, change_password,
								profile, profile_update )

urlpatterns = [
    url(r'^register/', user_register, name="register"),
    url(r'^login/', user_login, name="login"),
    url(r'^logout/', user_logout, name="logout"),
    url(r'^change_password/', change_password, name="change_password"),
    url(r'^profile/(?P<user_id>[0-9]+)', profile, name="profile"),
    url(r'^profile/update/(?P<user_id>[0-9]+)', profile_update, name="profile_update"),
]

# (?P<blog_id>[0-9]+)