from django.shortcuts import render
from django.views.generic import  View
from django.http import HttpResponse,JsonResponse
from .models import  Update
from django.core.serializers import serialize



class JsnCBV(View):
    def get(self,request,*args,**kwargs):
        data={
            "count":1000,
            "name":"shalin"
        }

        return JsonResponse(data)

class SearializedDetailView(View):
    def get(self,request,*args,**kwargs):
        obj=Update.objects.get(id=1)
        json_data=obj.serialize()
        return HttpResponse(json_data,content_type='application/json')

class SearializedListView(View):
    def get(self,request,*args,**kwargs):
        qs=Update.objects.all()
        json_data=serialize('json',qs,fields=('user','content'))
        return HttpResponse(json_data,content_type='application/json')