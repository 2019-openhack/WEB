#from django.views.generic.edit import FormView
#from .forms import fileUploadForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings

#from .forms import PDForm

import os

def handle_uploaded_file(user,pdf):
    with open(os.path.join(settings.MEDIA_ROOT,user, pdf.name), 'wb+') as destination:
            for chunk in pdf.chunks():
                destination.write(chunk)

@login_required(login_url='/login')
def file_upload(request):
    # 실제 파일을 올리는 요청
    if request.method == 'POST':
        pdf = request.FILES['file']
        user_name = request.session['user_name']
        #파일을 저장하는 부분
        #fs = FileSystemStorage()
        #filename = fs.save(pdf.name, pdf) 
        
        if not os.path.isdir(os.path.join(settings.MEDIA_ROOT,user_name)):
            os.mkdir(os.path.join(settings.MEDIA_ROOT,user_name))

        handle_uploaded_file(user_name, pdf)


        print(request.FILES)        
        print("file upload")

    # file 올리는 form 내놔라    
    else:
        user_name = request.session['user_name']
        request.session['path'] = os.path.join(str(user_name)) 
        print(request.session['path'])
        # 파일을 받을 준비를 하자
        

    #request.session['path'] = os.path.join(str(user
        

    return render(request, 'file_upload/index.html',{})



def sendRequest(request):
    if request.method == 'POST':
        print(os.getcwd())
        print("POST method")

    return render(request, 'file_upload/good.html',{})

'''
# Create your views here.
def file_upload2(request):
    form = fileUploadForm()
    if request.method == 'POST':
        print(os.getcwd())
        print("POST method")
        form = fileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            for count, x in enumerate(request.FILES.getlist("files")):
                def handle_uploaded_file(f):
                    with open(os.path.join(os.getcwd(),"media", f.name),'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
                handle_uploaded_file(x)
                print(x.name)
                os.remove("media/"+str(x.name))
                print(str(x.name)+"삭제완료")
            context = {'form':form,}
            return render(request, 'file_upload/index.html', context)
            # return HttpResponse(" File uploaded! ")
    else:
        form = fileUploadForm()

    return render(request, 'file_upload/index.html', {'form': form})
'''
   
