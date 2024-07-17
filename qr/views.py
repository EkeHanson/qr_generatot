import qrcode
from django.http import HttpResponse
from django.shortcuts import render

def generate_qr(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        img = qrcode.make(data)
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        return response
    return render(request, 'qr/generate.html')
