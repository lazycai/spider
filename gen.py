# coding: utf-8
import glob
import os
import sys
import os
from pyPdf import PdfFileWriter, PdfFileReader
import config
from config import *

reload(sys)
sys.setdefaultencoding('utf8')
def append_pdf(input, output):
    [output.addPage(input.getPage(page_num))
     for page_num in range(input.numPages)]

output = PdfFileWriter()


os.chdir(base_arch)

print '开始生成相关页面数据'
for x in glob.glob("*.html"):
    if x=='cover.html':
        os.system((u'wkhtmltopdf -s A4  -T 22mm -L 0mm -R 0mm   %s %s.pdf')%(x,x.split('.')[0]))
    else:
        os.system((u'wkhtmltopdf -s A4  --header-html '+base_folder+'res/header.html -T 22mm -L 0mm -R 0mm   %s %s.pdf')%(x,x.split('.')[0]))
    print x


print '开始合成'
for x in gen_list:
    append_pdf(PdfFileReader(file(base_folder+x+'.pdf','rb')),output)

output.write(file(base_folder+"combined.pdf", "wb"))
