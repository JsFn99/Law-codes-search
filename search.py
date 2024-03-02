import extract

def search(pdf, word):
    text = extract.extract_text_pdf(pdf)
    for page, content in text.items():
        if word in content:
            print(f'Page {page}: {content}')
            

def search_article(pdf, word):
    text = extract.extract_text_pdf(pdf)
    articles = {}
    current_article = None

    for page, content in text.items():
        lines = content.split('\n')
        for line in lines:
            if line.startswith('Article'):
                current_article = line
            elif current_article and word in line:
                articles[current_article] = line

    return articles
        
def print_result(result):
    for article, content in result.items():
        print(f'{article}: {content}')
        



