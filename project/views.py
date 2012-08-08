#-*- coding: gb2312 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.template.context import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic.simple import direct_to_template
from models import runners
import time
from django.core import serializers
from django.utils import simplejson


def home(request, template_name = 'project/index.html'):
    return render(request, template_name, {})

def updatetime(request):
    t = time.localtime()
    info = "%d/%d/%d:%d:%d:%d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    return HttpResponse(info)

class JsonResponse(HttpResponse):
    def __init__(self, data):
        content = simplejson.dumps(data,
                                   indent=2,
                                   ensure_ascii=False)
        super(JsonResponse, self).__init__(content=content,
                                           mimetype='application/json; charset=utf8')

def getRunners(request):
    t = []
    results = runners.objects.all()
    for r in results:
        t.append({'last_name':r.last_name, 'first_name':r.first_name, 'gender': r.gender, 'finish_time':r.finish_time})
    #json_serializer = serializers.get_serializer("json")()
    #res = json_serializer.serialize(t, ensure_ascii=False, indent=2)

    #return HttpResponse(res, mimetype="application/json; charset=utf8")
    return JsonResponse(t)

def addRunner(request):
    print "addRunner in invoked"
    try:
        if request.is_ajax():
            if request.method == 'GET':
                message = "This is an XHR GET request"
            elif request.method == 'POST':
                #print request.raw_post_data
                #req = simplejson.loads(request.raw_post_data[0], encoding="utf-8")
                root = request.POST
                first_name = root['txtFirstName']
                last_name = root['txtLastName']
                gender = root['ddlGender']
                finish_time = root['txtMinutes'] + ":" + root['txtSeconds']

                print first_name, last_name, gender, finish_time
                r = runners(first_name=first_name, last_name=last_name, gender=gender, finish_time=finish_time)
                r.save()
                message = 'ok'
        else:
            message = "No XHR"
    except :
        import sys
        message = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])

    return JsonResponse({'status':'success','message':message})
    #try:
    #    if request.method == 'POST':
    #        req = simplejson.loads(request.raw_post_data)
    #        first_time = req['txtFirstName']
    #        last_time = req['txtLastName']
    #        gender = req['ddlGender']
    #        finish_time = req['txtMinutes'] + ":" + req['txtSeconds']

    #        print first_time, last_time, gender, finish_time
    #except:
    #    import sys
    #    info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    #    return JsonResponse({'status':'fail','message':info})
    #else:
    #    return JsonResponse({'status':'success','message':'ok'})