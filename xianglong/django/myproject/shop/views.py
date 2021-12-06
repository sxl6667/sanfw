from django.shortcuts import render, HttpResponse
import json
# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def test(request):
    return render(request, 'test/index2.html', {
        'msg': 'hello',
        'class': 'reds'
    })

def test_json(request):
    if request.method == 'POST':
        return HttpResponse(json.dumps({
            'data': {
                'class': 'red'
            },
            'status': 1
        }))
    return HttpResponse('no')