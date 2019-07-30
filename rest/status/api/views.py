from rest_framework import generics,mixins,permissions
from rest_framework.authentication import SessionAuthentication
import json
from status.api.serializers import StatusSerializer
from status.models import Status
from django.shortcuts import get_object_or_404
from rest.rest_conf.pagination import  ShalinPag

from accounts.api.permissions import IsOwnerOrReadOnly

def is_json(json_data):
    try:
        real_json=json.loads(json_data)
        is_valid =True
    except ValueError:
        is_valid=False
    return is_valid

class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes          =   [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    # authentication_classes      =   [SessionAuthentication]
    serializer_class            =   StatusSerializer
    passed_id                   =   None
    # pagination_class             =ShalinPag

    def get_queryset(self):
        request=self.request
        print(request.user)
        qs= Status.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.filter(content__icontains=query)
        return qs
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    # def get_object(self):
    #     request     =   self.request
    #     passed_id   =   request.GET.get('id',None) or self.passed_id
    #     queryset    =    self.get_queryset()
    #     obj=None
    #     if passed_id is not None:
    #         obj=get_object_or_404(queryset,id=passed_id)
    #         self.check_object_permissions(request,obj)
    #     return  obj
    #
    # def get(self,request,*args,**kwargs):
    #     url_passed_id   =   request.GET.get('id')
    #     json_data       =   {}
    #     body            =   request.body
    #     if is_json(body):
    #         json_data       =   json.loads(request.body)
    #     new_passed_id   =   json_data.get('id',None)
    #     # print (request.body)
    #
    #     passed_id=new_passed_id or url_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(request,*args,**kwargs)
    #     return super(StatusAPIView, self).get(request,*args,**kwargs)


    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self,request,*args,**kwargs):
    #     url_passed_id = request.GET.get('id')
    #     json_data = {}
    #     body = request.body
    #     if is_json(body):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     # print (request.body)
    #
    #     passed_id = new_passed_id or url_passed_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self,request,*args,**kwargs):
    #     url_passed_id = request.GET.get('id')
    #     json_data = {}
    #     body = request.body
    #     if is_json(body):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     # print (request.body)
    #
    #     passed_id = new_passed_id or url_passed_id or None
    #     self.passed_id = passed_id
    #     return self.update(request, *args, **kwargs)
    #
    # # def perform_destroy(self,instance):
    # #     if instance is not None:
    # #         return instance.delete()
    # #     return None
    # def delete(self,request,*args,**kwargs):
    #     url_passed_id = request.GET.get('id')
    #     json_data = {}
    #     body = request.body
    #     if is_json(body):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     # print (request.body)
    #
    #     passed_id = new_passed_id or url_passed_id or None
    #     self.passed_id = passed_id
    #     return self.destroy(request, *args, **kwargs)


# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes          =   []
#     authentication_classes      =   []
#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer

class StatusDetailAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
    permission_classes          =   [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes      =   []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id'

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)
#
# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #     permission_classes          =   []
# #     authentication_classes      =   []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer
# #     lookup_field                = 'id'
#
# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #     permission_classes          =   []
# #     authentication_classes      =   []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer
# #     lookup_field                = 'id'