import pdfkit 
import os
from PyPDF2 import PdfFileWriter, PdfFileReader,PdfFileMerger

methods = {'single':'hamming',
           'complete':'hamming',
           'average':'hamming',
           'ward':'euclidean' }

path = os.getcwd()
for method in methods.keys():
	if method=='single':
		continue
	os.chdir(path+'/'+method)
	for file in os.listdir():
		if method == 'complete':
			continue
		if file.endswith('.html'):
			name,_ =file.split('.')
			print(name)
			pdfkit.from_file(file, f'{name}.pdf')

	pdf_merger = PdfFileMerger()
	for file in os.listdir():
		if file.endswith('.pdf'):
			pdf_merger.append(file)


	with open(f'{method}.pdf', 'wb') as fileobj:
		pdf_merger.write(fileobj)













# for method in methods.keys():
# 	if method=='single':
# 		continue
# 	print(method)
# 	for file in os.listdir(method):
# 		if file.endswith('.html'):
# 			name,_ =file.split('.')
# 			print(name)
# 			pdfkit.from_file(f'{method}/{file}', f'{method}/{name}.pdf')

# 	pdf_merger = PdfFileMerger()
# 	for file in os.listdir(method):
# 		if file.endswith('.pdf'):
# 			pdf_merger.append(f'{method}/{file}')


# 	with open('{method}/{method}.pdf', 'wb') as fileobj:
# 		pdf_merger.write(fileobj)
