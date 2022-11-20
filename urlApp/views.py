from django.shortcuts import render, redirect
import uuid
from . models import LinkInfo
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    if request.method == 'POST':
        link = request.POST['link']
        linkID = str(uuid.uuid4())[:5]
        new_link = LinkInfo(link=link,linkID = linkID)
        new_link.save()
        return HttpResponse(linkID)
    
def newUrl(request, p):
    linkID = LinkInfo.objects.get(linkID = p)
    return redirect(linkID.link)