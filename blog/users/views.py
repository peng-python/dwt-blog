# from django.shortcuts import render
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth import authenticate,login,logout
# from django.http import HttpResponse,HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import mixins,status
from rest_framework import viewsets,authentication,permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .serializers import UserDetailSerializer,UserRegSerializer

User = get_user_model()

from users.models import UserModel
from users.forms import RegisterForm,LoginForm
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewSet(CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return UserDetailSerializer
    #     elif self.action == 'create':
    #         return UserRegSerializer
    #
    #     return UserDetailSerializer
    #
    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return [permissions.IsAuthenticated()]
    #     elif self.action == 'create':
    #         return []
    #
    #     return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['nick_name'] = user.nick_name if user.nick_name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()



# class RegViewSet(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     serializer_class = UserRegSerializer
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     mobile = serializer.validated_data['mobile']
    #     record =


# def register(request):
#     request_form=RegisterForm(request.POST)
#     if request_form.is_valid():
#         post=request.POST
#         user_name=post.get('user_name','')
#         pass_word1=post.get('pass_word1','')
#         pass_word2=post.get('pass_word2','')
#         if pass_word1 != pass_word2:
#             return render(request,'users/register.html')
#         email=post.get('email','')
#         users=UserModel()
#         users.username=user_name
#         users.password=make_password(pass_word2)
#         users.email=email
#         users.save()
#         return render(request,'blog/index.html')
#     else:
#         return render(request,'users/register.html')
#
#
# def login_user(request):
#     login_form=LoginForm(request.POST)
#     if login_form.is_valid():
#         post=request.POST
#         user_name=post.get('username','')
#         pass_word=post.get('password','')
#         user=authenticate(username=user_name,password=pass_word)
#         if user is not None:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return render(request,'users/register.html')
#         else:
#             return render(request,'users/register.html')
#     else:
#         return render(request,'users/register.html')
#
#
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))