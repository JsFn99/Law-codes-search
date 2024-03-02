# PDF Text Extraction and Search

This project is a Python application designed to extract text from PDF files and provide search functionalities within the extracted content. The application utilizes the PyPDF2 library for PDF processing. The primary features include extracting text from PDFs, printing the content of each page, and searching for specific words or articles within the document.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/JsFn99/Law-codes-search.git
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install PyPDF2
   ```

## Usage

### Extracting Text from PDF

To extract and print the text content of each page from a PDF file, you can use the following code:

```python
from extract import extract_text_pdf, print_pdf

pdf_path = '/path/to/your/pdf/file.pdf'
text_from_pdf = extract_text_pdf(pdf_path)
print_pdf(text_from_pdf)
```

### Searching for a Word in the PDF

To search for a specific word in the entire PDF document and print the pages where the word is found, use the following code:

```python
from search import search

pdf_path = '/path/to/your/pdf/file.pdf'
search(pdf_path, 'your_search_word')
```

### Searching for an Article in the PDF

To search for an article containing a specific word in the PDF and print the relevant content, use the following code:

```python
from search import search_article, print_result

pdf_path = '/path/to/your/pdf/file.pdf'
result = search_article(pdf_path, 'your_search_word')
print_result(result)
```

## Project Structure

- **extract.py:** Contains functions for extracting text from PDF files and printing the content of each page.

- **search.py:** Implements functions for searching specific words or articles within the extracted text.

- **main.py:** An example script demonstrating the usage of functions from both extract.py and search.py.

## Example

You can run the provided `main.py` script as an example:

```bash
python main.py
```

Replace the `pdf_path` variable in `main.py` with the path to your desired PDF file.

Feel free to customize and extend the code according to your specific requirements.
