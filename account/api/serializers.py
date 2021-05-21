# from django.db.models import fields
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from account.models import Account
# # from django.contrib.auth.models import User
# # from typing_extensions import Required



# class RegistrationSerializer(serializers.ModelSerializer):

#     password2 = serializers.CharField(style={'input_type': 'password'}, min_length=8, write_only=True)
#     class Meta:
#         model = Account
#         fields = ("email", "username", "password", "password2")
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
    
#     def save(self):
#         account = Account(
#             email=self.validated_data['email'],
#             username=self.validated_data['username']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password2 != password:
#             raise serializers.ValidationError({'password': 'Passwords don\'t match'})
        
#         account.set_password(password)
#         account.save()
        
#         return account