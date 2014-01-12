from django.conf.urls import patterns, url, include
from django.contrib import admin

from two_factor.admin import AdminSiteOTPRequired
from two_factor.views import LoginView

from .views import SecureView, SecureRaisingView

admin.autodiscover()
otp_admin_site = AdminSiteOTPRequired()

urlpatterns = patterns(
    '',
    url(
        regex=r'^account/logout/$',
        view='django.contrib.auth.views.logout',
        name='logout',
    ),
    url(
        regex=r'^account/custom-login/$',
        view=LoginView.as_view(redirect_field_name='next_page'),
        name='custom-login',
    ),
    url(
        regex=r'^secure/$',
        view=SecureView.as_view(),
        name='secure-view',
    ),
    url(
        regex=r'^secure/raises/$',
        view=SecureRaisingView.as_view(),
        name='secure-view',
    ),
    url(r'', include('two_factor.urls', 'two_factor')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^otp_admin/', include(otp_admin_site.urls)),
)