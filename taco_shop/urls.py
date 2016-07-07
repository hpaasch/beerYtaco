
from django.conf.urls import url, include
from django.contrib import admin

from taco_app.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    # url(r'^create_account/$', CreateAccountView.as_view(), name='create_account_view'),
    url(r'^$', IndexView.as_view(), name='index_view'),

]
