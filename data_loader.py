import os
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import urllib.request

class data_loader:
    def __init__(self, folder, filename,type):
        self.folder = folder
        self.filename =filename
        self.type = type
    
    def load_text(self):
        file = open(self.filename, 'r', encoding='utf-8')
        content = file.read()
        return content

    def load_pdfs(self):
        documents = []
        filenames = []
        for pdf_file in os.listdir(self.filename):
            if pdf_file.endswith('.pdf'):
                file_path = os.path.join(self.folder, pdf_file)
                with open(file_path, 'rb') as file:
                    reader = PdfReader(file)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text()
                    documents.append(text)
                    filenames.append(pdf_file)
        return documents, filenames
    
    def load_html(self):
        html_doc =urllib.request.urlopen(self.html_url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

html_doc = data_loader.load_html("http://www.python.org")
print(html_doc)


