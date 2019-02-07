from rest_framework import serializers
from userprofile.models import UserProfile


'''
Serializer -> converts into JSON
Serializer ->does Validations on data
'''
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'phone_no',
            'gender',
            'birth_date',
        ]
        read_only_fields = ['user'] #now this is read only, we cant see them in put and post

    # def validate_content(self,value):
    #     if len(value)>1000:
    #         raise serializers.ValidationError("This is wayy to long.")
    #     return value

    # def validate(self, data):
    #     content = data.get("content", None)
    #     if content == "":
    #         content = None
    #     image = data.get("image", None)
    #     if content is None and image is None:
    #         raise serializers.ValidationError("Content or image i required.")
    #     return data
'''
    from userprofile.models import UserProfile
    from userprofile.api.serializers import UserProfileSerializer
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser


#Running shell examples

    profile = UserProfile.objects.all()
    serializer = UserProfileSerializer(profile)
    serializer.data
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    # snippet = Snippet(code='print "hello, world"\n')
    # snippet.save()
    
    
    #for singer object
    obj = UserProfile.objects.first()
    serializer = UserProfileSerializer(obj)
    serializer.data
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)

    stream = BytesIO(json_data)
    data = JSONParser().parse(stream)
    print(data)

'''