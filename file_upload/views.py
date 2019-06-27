#from django.views.generic.edit import FormView
#from .forms import fileUploadForm
from django.shortcuts import render


def file_upload(request):
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
   
