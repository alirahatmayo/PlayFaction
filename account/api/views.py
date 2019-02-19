import json
from .serializers import AccountSerializer
# from account.models import Account
from rest_framework import generics, mixins , permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from rest_framework.response import Response
from account.models import Account


'''
Making create and List Api view in single class
CreateModelMixin----->POST Method
UpdateModelMixin----->PUT Method

'''

#creating method for checking if data is json,
def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid




class AccountAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):
    permission_classes = [] #post put method if authenticated, else just read only
    authentication_classes = []
    serializer_class = AccountSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        #print(request.user)
        qs = Account.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(remarks__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):           # will let you add without defining user id in text area
    #     serializer.save(user=self.request.user)





class AccountAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class            = AccountSerializer
    queryset                    = Account.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def balance_update(self,sender, receiver, amount):
