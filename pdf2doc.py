from pdf2docx import converter
pdf_file = 'PDF name.pdf'
docx_file = 'Sample.docx'
cv = converter(pdf_file)
cv.convert(docx_file)
cv.close()