from account.api.views import AccountAPIDetailView, AccountAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', AccountAPIView.as_view()),
    # url(r'^$', UserProfileAPIDetailView.as_view()),
    url(r'^(?P<id>\d+)/$', AccountAPIDetailView.as_view()),
    # url(r'^(?P<id>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>\d+)/delete/$', StatusDeleteAPIView.as_view()),

]