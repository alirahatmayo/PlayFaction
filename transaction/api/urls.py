from transaction.api.views import TransactionAPIDetailView, TransactionAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', TransactionAPIView.as_view()),
    # url(r'^$', UserProfileAPIDetailView.as_view()),
    url(r'^(?P<id>\d+)/$', TransactionAPIDetailView.as_view()),
    # url(r'^(?P<id>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>\d+)/delete/$', StatusDeleteAPIView.as_view()),

]