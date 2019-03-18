# pdf_splitter.py

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path, split_number):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)

    pdf_writer = PdfFileWriter()

    for page in range(split_number-1):
        pdf_writer.addPage(pdf.getPage(page))

    output_filename = '{}_page_{}.pdf'.format(fname, 1)

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    print('Created: {}'.format(output_filename))


    pdf_writer = PdfFileWriter()

    for page in range(split_number-1, pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))

    output_filename = '{}_page_{}.pdf'.format(fname, split_number)

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    print('Created: {}'.format(output_filename))



if __name__ == '__main__':
    path = 'test.pdf'
    split_number = 3
    pdf_splitter(path, split_number)
