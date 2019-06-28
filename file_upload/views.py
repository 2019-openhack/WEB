#from django.views.generic.edit import FormView
#from .forms import fileUploadForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponseRedirect

#from .forms import PDForm

from collections import Counter 
from .preprocessing import preprocessing as prep
import os
import shutil
import glob
import pandas as pd
import plotnine
from plotnine import *

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
        #파일을 업로드하는 부분
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

        #처음 들어올 때 다 지움
        if os.path.isdir(os.path.join(settings.MEDIA_ROOT,user_name)):
            shutil.rmtree(os.path.join(settings.MEDIA_ROOT,user_name))

        print(request.session['path'])
        # 파일을 받을 준비를 하자
        

    #request.session['path'] = os.path.join(str(user
        

    return render(request, 'file_upload/index.html',{})

def visualization(result, path):
    
    sorted_cnt = sorted(result.items(), key=lambda t : t[1],reverse=True)
    df = pd.DataFrame(sorted_cnt[:30],columns=['word','freq'])

    df = pd.DataFrame({
        'word' : sorted_keys[:30] * 2,
        'freq' : sorted_values[:30] * 2
    })


    p = (ggplot(df)
     + geom_col(aes(x='word',y='freq',fill='word'))
     + scale_color_hue(l=0.45)                                  # some contrast to make the lines stick out
     + ggtitle('Greek Letter Analysis')
     + theme(axis_text_x=element_text(angle=45, hjust=1))
    )

    ggsave(plot = p, filename = "img", path = path)

def makeDic(request):
    user_name = request.session['user_name']
    file_folder = os.path.join(settings.MEDIA_ROOT,user_name)
    #폴더가 있으면 단어 분석을 시작한다.
    if os.path.isdir(file_folder):
        print(file_folder)
        #모든 파일을 가져옴
        pdf_path = glob.glob(file_folder+"/*.pdf")
        txt_path = glob.glob(file_folder+"/*.txt")
       
        path_list = pdf_path + txt_path
    
        result = Counter('')
        
        #예문을 만들기 위한 path
        text_path = []

        print(path_list)
        for path in path_list:
            if path[-3:] == 'pdf':
                pdf = prep(input_path = path)
                output_path = pdf.pdf2txt()
                text_path.append(output_path)

                pdf.clean_text()
                cnt = pdf.word_Frequency()

            elif path[-3:] == 'txt':
                txt = prep(output_path = path)
                text_path.append(path)

                txt.clean_text()
                cnt = txt.word_Frequency()

            result += cnt
            print(cnt)


    return render(request, '/index.html',{})

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
   
