# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, 'show_madadjoo.html')

# Create your views here.