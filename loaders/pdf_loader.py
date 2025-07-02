from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class PDFLoader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
    
    def load(self):
        loader = PyMuPDFLoader(self.pdf_path)
        content = loader.load()
        
        # Clean each document's text content
        cleaned_content = [
            Document(page_content=doc.page_content.replace("\n", " ").replace("\t"," ").replace("  "," "), metadata=doc.metadata)
            for doc in content
        ]

        return cleaned_content