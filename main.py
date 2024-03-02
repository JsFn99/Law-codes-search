from extract import extract_text_pdf, print_pdf
from search import search, search_article, print_result


pdf_path = '/Users/mac/Code/Law_Project/CODES_DROIT_PDF/code penal.pdf'
text_from_pdf = extract_text_pdf(pdf_path)
print_pdf(text_from_pdf)
search(pdf_path, 'peine')
result = search_article(pdf_path, 'incendie')
print_result(result)