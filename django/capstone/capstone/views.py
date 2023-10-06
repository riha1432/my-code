from django.http import HttpResponse
from django.shortcuts import render

def claude(request):
    
    # HTML 파일에 넘겨줄 추가 내역들 삽입하는 곳
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'templates/video.html')