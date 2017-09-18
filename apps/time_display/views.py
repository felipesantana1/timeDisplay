# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime

def index(request):
    context = {

        'time': strftime('%b-%d-%Y %I:%M %p', localtime())

    }
    return render(request,'time_display/page.html', context)