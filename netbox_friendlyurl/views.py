# views.py
from django.apps import apps
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import resolve
from numbers import Number

def RedirectView(request, **kwargs):
    
    django_numberfields = [
        'AutoField',
        'BigAutoField',
        'BigIntegerField',
        'DecimalField',
        'DurationField',
        'FloatField',
        'IntegerField',
        'PositiveBigIntegerField',
        'PositiveIntegerField',
        'PositiveSmallIntegerField',
        'SmallAutoField',
        'SmallIntegerField',
    ]

    django_nontextfields = [
        'AutoField',
        'BigAutoField',
        'BigIntegerField',
        'BinaryField',
        'BooleanField',
        'DateField',
        'DateTimeField',
        'DecimalField',
        'DurationField',
        'FloatField',
        'IntegerField',
        'PositiveBigIntegerField',
        'PositiveIntegerField',
        'PositiveSmallIntegerField',
        'SmallAutoField',
        'SmallIntegerField',
        'TimeField',
    ]



    params = kwargs['match']
    urlparts = [p for p in params.split('/') if p]

    applabel = urlparts.pop(0)
    modelurl = urlparts.pop(0)
    urlparts='/'.join(urlparts).split('|')  # delimiter is |, but a / in a prefix splits it in parts.

    appraw = resolve(f"/{applabel}/{modelurl}/")
    modelname = appraw.url_name[:-5]  # strip _list from the name
    furl_model = apps.get_model(applabel, modelname)

    modelsearchdata = {}
    for data in urlparts:
        datakey, datavalue = data.split('=')
        fieldtype=furl_model._meta.get_field(datakey).get_internal_type()
        if fieldtype == 'ForeignKey':
            fieldtype=furl_model._meta.get_field(datakey).target_field.get_internal_type()
            if (fieldtype in django_numberfields) and not isinstance(datavalue,Number):
                try:
                    resolveddatavalue=furl_model._meta.get_field(datakey).remote_field.model.objects.filter(Q(name__iexact=datavalue))
                    if len(resolveddatavalue) == 1:
                        datavalue=resolveddatavalue[0].id
                    else:
                        datavalue = ''
                except:
                    datavalue=''


        if datavalue:
            modelsearchdata[datakey]=datavalue

    furl_objects = furl_model.objects.filter( **modelsearchdata)

    if len(furl_objects) == 0:
        for key in list(modelsearchdata):
            if furl_model._meta.get_field(key).get_internal_type() == 'ForeignKey':
                fieldtype=furl_model._meta.get_field(key).target_field.get_internal_type()
            else:
                fieldtype=furl_model._meta.get_field(key).get_internal_type()
            if fieldtype not in django_nontextfields:
                modelsearchdata[key+'__istartswith']=modelsearchdata.pop(key)
        furl_objects = furl_model.objects.filter( **modelsearchdata)

    if len(furl_objects) == 1:
        return redirect(furl_objects[0].get_absolute_url())

    searchvalue=list(modelsearchdata.values())[0]

    # return redirect(f"/search/?lookup=icontains&obj_types={applabel}.{modelname}&q={searchvalue}")  #icontains is a valid lookup value, but not accepted ?
    return redirect(f"/search/?obj_types={applabel}.{modelname}&q={searchvalue}")
