import PyPDF4
def pdftotxtconverter():
    with open('input1.pdf','rb') as fp:
        pdfReader = PyPDF4.PdfFileReader(fp)
        for i in range(pdfReader.getNumPages()):
            with open(f'output{i}.txt','w') as fr:
                fr.write(pdfReader.getPage(i).extractText())
        return pdfReader.getNumPages()            

            # os.remove(f'output{i}.txt')

pdftotxtconverter()