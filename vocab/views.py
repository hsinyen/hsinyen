from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response


def index (request):
    return render_to_response('fluid.html',
                              {'message': 'bye'})
