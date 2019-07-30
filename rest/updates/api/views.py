import json

from updates.models import  Update
from django.views.generic import View
from  django.http import HttpResponse
from django.core.serializers import serialize
from updates.mixins import CsrfMixins

from updates.forms import UpdateModelForm


class UpdateModelDetaiApiView(CsrfMixins,View):
    def get_object(self,id=None):
        qs = Update.objects.filter(id=id)
        print(qs)
        if qs.count()==1:
            return qs.first()
        return None

    def get(self,request,id,*args,**kwargs):
        obj=Update.objects.get(id=id)
        json_data=obj.serialize()

        return HttpResponse(json_data,content_type='application/json')



    def put(self,id, request, *args, **kwargs):
        obj=self.get_object(id=id)
        if obj is None:
            error_data=json.dumps({"message:""update not found"})
            return HttpResponse(error_data,content_type='application/json')
        json_data={"message":"not found"}
        return HttpResponse(json_data,content_type='application/json')


    def delete(self, request,id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message:""update not found"})
            return HttpResponse(error_data, content_type='application/json')
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')




class UpdateModelListApiView(CsrfMixins,View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data=serialize('json',qs,fields=('user','content','image','id'))

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        form=UpdateModelForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=True)
            obj_data=obj.serialize()
            return HttpResponse(obj_data, content_type='application/json')
        if form.errors:
            data=json.dumps(form.errors)
            return HttpResponse(data, content_type='application/json')
        data={"message":"not alllowed"}
        return HttpResponse(data, content_type='application/json')
    def put(self, request, *args, **kwargs):
        return  # json

    def delete(self, request, *args, **kwargs):
        return  # json