from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from Macao import models
import os


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        obj = request.FILES.get('fafafa')
        # f = open(os.path.join('uploadFiles', obj.name), 'wb')
        f = open('d:\\upload\\' + obj.name, 'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        # return HttpResponse('上传成功')
        return render(request, "index.html", {"data": "上传成功"})
