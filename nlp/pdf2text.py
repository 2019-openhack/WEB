# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:55:35 2019

@author: JM
"""

import os
import re
from tqdm import tqdm
from tkinter.filedialog import askopenfilename 
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter,resolve1
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter


def isExistFile(path):
    file_name = path.split('/')[-1]
    
    for i in os.listdir("."):
        if file_name == i:
            return True
        
    return False

def pdf2txt(input_path):
    '''
    input_path : str, PDF File
    
    =============================
    
    return : str, text File path
    '''
    
    # input
    password=''
    pagenos=set()
    maxpages=0
    
    # output
    imagewriter = None
    rotation = 0
    codec = 'UTF-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    
    infp = open(input_path,"rb")
    
    output_path = input_path[:-4] + '_trans.txt'
    
    outfp = open(output_path,"w",encoding='UTF8')
    
    #page total num
    parser = PDFParser(infp)
    document = PDFDocument(parser)
    page_total_num = resolve1(document.catalog['Pages'])['Count']
    
    #
    rsrcmgr = PDFResourceManager(caching=caching)

    # pdf -> text converter
    device = TextConverter(rsrcmgr,
                           outfp,
                           codec=codec,
                           laparams=laparams, 
                           imagewriter=imagewriter)

    # pdf -> text interpreter
    interpreter = PDFPageInterpreter(rsrcmgr,device)
    
    # pdf -> text start
    with tqdm(total=page_total_num) as pbar:
        for page in PDFPage.get_pages(infp,
                                      pagenos,
                                      maxpages,
                                      password=password,
                                      caching=caching,
                                      check_extractable=True):

            page.rotate = (page.rotate+rotation) % 360     
            interpreter.process_page(page)
            
            pbar.update(1)

    print('==== success ====')

    outfp.close()
    infp.close()
    
    return output_path
    
def clean_text(path):
    '''
    path : str, text File Path
    
    
    ===========================
    
    return : list, sentences
    '''
    
    f = open(path,"rb")
    line_list = []
    
    while True:
        line = f.readline()
        line_list.append(line)
        if not line: break
    
    # remove nextline
    word = b" ".join(line_list).split()
    sentences = b" ".join(word)
    
    
    # remove ASCII
    # define pattern 
    pattern = re.compile(b"[\x80-\xff]")
    sentences = re.sub(pattern,b"",sentences)
    
    sentences = sentences.split(b". ")
    
    cleaned_txt = []
    
    for sentence in sentences:
        sentence = sentence.replace(b"- ",b'')
        sentence = sentence.replace(b"-",b'')
        cleaned_txt.append(sentence)
    
    f.close()
    
    os.remove(path)
    
    return cleaned_txt

txt_path = pdf2txt('C:/Users/JM/Desktop/MCNN.pdf')
cleaned_text = clean_text(txt_path)
print(cleaned_text)