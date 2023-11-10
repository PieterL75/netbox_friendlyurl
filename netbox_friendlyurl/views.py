# views.py
from django.apps import apps
from django.shortcuts import redirect
from django.urls import resolve
import re

def RedirectView(request, **kwargs):
    
    params = kwargs['match']    
    urlparts = [p for p in params.split('/') if p]

    applabel = urlparts.pop(0)
    modelurl = urlparts.pop(0)

    appraw = resolve(f"/{applabel}/{modelurl}/")
    modelname = appraw.url_name[:-5]  # strip _list from the name

    modelsearchdata = {}
    for data in urlparts:
        datakey, datavalue = data.split('=')
        modelsearchdata[datakey]=datavalue

    furl_model = apps.get_model(applabel, modelname)
    furl_objects = furl_model.objects.filter( **modelsearchdata)
    if len(furl_objects) == 0:
        for key in list(modelsearchdata):
            if modelsearchdata[key][-2:].lower() != 'id':
                modelsearchdata[key+'__istartswith']=modelsearchdata.pop(key)
        furl_objects = furl_model.objects.filter( **modelsearchdata)

    if len(furl_objects) == 1:
        return redirect(furl_objects[0].get_absolute_url())

    searchvalue=list(modelsearchdata.values())[0]

    # return redirect(f"/search/?lookup=icontains&obj_types={applabel}.{modelname}&q={searchvalue}")  #icontains is a valid lookup value, but not accepted ?
    return redirect(f"/search/?obj_types={applabel}.{modelname}&q={searchvalue}")
