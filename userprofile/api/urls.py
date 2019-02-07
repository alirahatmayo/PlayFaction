from userprofile.api.views import UserProfileAPIDetailView
from django.conf.urls import url

urlpatterns = [
    # url(r'^$', StatusListSearchAPIView.as_view()),
    # url(r'^$', UserProfileAPIDetailView.as_view()),
    url(r'^(?P<id>\d+)/$', UserProfileAPIDetailView.as_view()),
    # url(r'^(?P<id>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>\d+)/delete/$', StatusDeleteAPIView.as_view()),

]