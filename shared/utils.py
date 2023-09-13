from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import resolve1
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def get_pdf_pages_and_sizes(filename: str):
    """Ref https://stackoverflow.com/a/47686921"""
    with open(filename, "rb") as fp:
        parser = PDFParser(fp)
        document = PDFDocument(parser)
        num_pages = resolve1(document.catalog["Pages"])["Count"]
        page_sizes = [(int(page.mediabox[2]), int(page.mediabox[3])) for page in PDFPage.create_pages(document)]
        return num_pages, page_sizes
