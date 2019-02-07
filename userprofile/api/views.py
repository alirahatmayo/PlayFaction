import json
from .serializers import UserProfileSerializer
from userprofile.models import UserProfile
from rest_framework import generics, mixins , permissions
from rest_framework.authentication import SessionAuthentication


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


class UserProfileAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class            = UserProfileSerializer
    queryset                    = UserProfile.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)