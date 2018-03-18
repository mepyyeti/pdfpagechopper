#!usr/bin/env python3

#pdfpagechopper0.py

import PyPDF2, os, sys
from functools import partial

def my_user_input(question, type, errmsg):
	while True:
		asked = input(question)
		if asked !='':
			try:
				asked = type(asked)
			except ValueError:
				print(f'"{asked}" is invalid.')
				continue
			else:
				print('ok')
				return asked
		else:
			continue

def chopper():
	while True:
		os.chdir('/home/me/Downloads/')
		print(os.getcwd())
		
		str_question = partial(my_user_input,type=str,errmsg='err...something went wrong.')
		int_question = partial(my_user_input, type=int, errmsg='err...something went wrong\nDon\t forget u must user NUMBERS...')
		
		pdf_file_name = str_question('please enter filename >> ')
		pdf_file_opened = open(pdf_file_name, 'rb')
		
		reading = PyPDF2.PdfFileReader(pdf_file_opened)
		pdfWriter = PyPDF2.PdfFileWriter()
		
		pdflist= []
		printed_pdflist = []
		
		beginning = int_question('start at what page number? ')
		finish = int_question('end at what page number? ') 
		for num in range(beginning-1,finish):
			pdflist.append(num)
			printed_pdflist.append(num+1)
		print(f'your selected pages from {pdf_file_name} are: \n\t{printed_pdflist}')
		
		while True:
			choice = str_question('press \'y\' or \'yes\' to enter other pages or range of pages.')
			if choice == 'y' or choice == 'yes':
				beginning = int_question('start at what page number? ')
				finish = int_question('end at what page number? ') 
		
				if finish > reading.numPages:
					print(f'there aren\'t {finish} pages in {pdf_file_name}.')
					finish = int_question('end at what page number? ') 
					
					for num in range(beginning -1, finish):
						pdflist.append(num)
						print('corrected and added.')
				
				pdflist_adds = []
				for p in range(beginning, finish + 1):
					pdflist_adds.append(p)
					printed_pdflist.append(p)
			
				for num in range(beginning -1, finish):
					pdflist.append(num)
				print(f'you added pages --> {pdflist_adds}.')
				continue
			else:
				break
		
		
		if finish > reading.numPages:
			print(f'there aren\'t {finish} pages in {pdf_file_name}.')
			finish = int_question('end at what page number? ') 
		
			for num in range(beginning -1, finish):
				pdflist.append(num)
		
		else:
			print(f'your selected pages from {pdf_file_name} are: \n\t{printed_pdflist}.')
			for num in pdflist:
				new_page = reading.getPage(num)
				pdfWriter.addPage(new_page)
		
		new_file_name = str_question('please enter new filename WITH .pdf ext...')
		with open(new_file_name, 'wb') as new_pdf_file:
			pdfWriter.write(new_pdf_file)
	
		choice = str_question('enter \'g\' or \'go\' to go again >> ')
		if choice == 'g' or choice == 'go':
			continue
		else:
			sys.exit()


if __name__ == '__main__':
	chopper()
else:
	print(f'{__name__} is a walled garden sir.  DO NOT taint it with inferior associations.')
	sys.sleep(2)
	print('Good day to you.')
