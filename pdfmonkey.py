import glob, os, sys
from PyPDF2 import PdfFileWriter, PdfFileReader

def grab_page_1():
    pdf_paths = glob.glob('./input/*.pdf')

    print("Found {:3d} PDF files".format(len(pdf_paths)))

    for pdf in pdf_paths:
        output = PdfFileWriter()
        input1 = PdfFileReader(open(pdf, "rb"))

        output.addPage(input1.getPage(0))

        base_name = os.path.basename(pdf)
        output_filename = "./output/{}_f.pdf".format(os.path.splitext(base_name)[0])

        print("Processing '{}'".format(base_name))

        outputStream = open(output_filename, "wb")
        output.write(outputStream)

if __name__ == "__main__":
    grab_page_1()
