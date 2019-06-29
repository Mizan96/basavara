from django.conf.urls import url

from app_account.views import (
    contact,
    login,
    logout,
    signup
)

urlpatterns = [
    url(r'^contact/$', contact, name='contact'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]