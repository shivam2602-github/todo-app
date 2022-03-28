from django.shortcuts import render,redirect
from . models import Enquiry
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your views here.
def index(request):
    enq = Enquiry.objects.all()
    context={'enqq':enq}
    return render(request, 'index.html',context)
def enquiry(request):
    return render(request,'enquiry.html')
def new(request):
    name = request.POST['fname']
    address = request.POST['address']
    conttno = request.POST['coo']
    emailaddress = request.POST['emailaddress']
    enqurytext = request.POST['enquirytext']
    e = Enquiry(name=name, address=address, no=conttno, emailaddress=emailaddress, enquirytext=enqurytext)
    e.save()
    return redirect('index')
def delete(request,id):
    e=Enquiry.objects.get(id=id)
    e.delete()
    return redirect('index')
def update(request,id):
    enq=Enquiry.objects.get(id=id)
    return render(request,'update.html',{'enqq':enq})
def updateenq(request):
    id=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    e=Enquiry( id=id,name=name, address=address, no=contactno, emailaddress=emailaddress, enquirytext=enquirytext)
    e.save()
    return redirect ('index')
def upload(request):#opens upload page
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        return render(request, 'upload.html',{'url':uploaded_file_url})
    return render(request, 'upload.html')









