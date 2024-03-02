from PyPDF2 import PdfReader

def extract_text_pdf(pdf):
    with open(pdf, 'rb') as file:
        reader = PdfReader(file)
        length = len(reader.pages)
        text = {0 : 'test'}
        for page_number in range(length):
            page = reader.pages[page_number]
            text[page_number + 1] = page.extract_text()  
    return text

#print the pdf with a for loop each key is a page number and each value is the text of the page
def print_pdf(text):
    for page, content in text.items():
        print(f'Page {page}: {content}')         

