import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO
from app import app
import re


def convert_pdf_to_text(path):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


def filter_resumes(resume, keywords):
    path = os.path.join(app.config['STATIC_PATH'], 'cv-uploads', resume)
    text = convert_pdf_to_text(path)
    for keyword in keywords:
        if re.search(keyword, text, re.IGNORECASE):
            return resume
