import srn_docs_api

from io import StringIO

from bs4 import BeautifulSoup

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def extract_text_from_srn_doc(fpath):
    """
    Tries to extract text from a downloaded SRN document. Currently, only PDF 
    and HTML are supported and page-wise extraction (obviously) ony works with 
    PDF.

    Args:
        fpath (str): The file path to a locally downloaded SRN document.

    Raises:
        Exception: Whenever either PDF and HTML text extraction fail.

    Returns:
        [str]: A list of strings containing text for each parsed page.
    """
    text = []
    try:
        with open(fpath, 'rb') as f:
            parser = PDFParser(f)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            text = []
            for page in PDFPage.create_pages(doc):
                output_string = StringIO()
                device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                interpreter.process_page(page)
                text.append(output_string.getvalue())

    except:
        print("File does not parse as PDF - trying HTML")

    if text == []:
        try:
            with open(fpath) as f:
                soup = BeautifulSoup(f, 'html.parser')
                is_html = bool(soup.find())
        
            if is_html:
                text = soup.get_text(' ', strip=True)
            else: 
                raise Exception()
        except:
            print("File is also not parseable as HTML - giving up")

    return text


if __name__ == "__main__":
    import random

    companies = srn_docs_api.get_srn_companies()
    documents = srn_docs_api.get_srn_documents()
    print("Searching comapny with a name containing 'Allianz'")
    matches = [c for c in companies if 'Allianz' in c['name']]
    print(
        f"Found {len(matches)} match(es). " +
        "Retrieving the documents for the first match."
    )
    docs = [d for d in documents if d['company_id'] == matches[0]['id']] 
    FPATH = 'test_srn_docs.pdf'
    print(
        f"Found {len(docs)} documents. " +
        "Retrieving the first document from the list " +
        f"and storing as '{FPATH}'."
    )
    srn_docs_api.download_document(docs[0]['id'], FPATH)
    print(
        "Parsing the text of the document into a page-wise list. " +
        "This might take a while ..."
    )
    tlist = extract_text_from_srn_doc(FPATH)
    if len(tlist) > 0:
        p = random.randint(0, len(tlist) - 1)
        print(
            f"Parsed {len(tlist)} document pages. " + 
            f"This is the text for the randomly parsed page {p}:\n\n" + 
            tlist[p] + "\n\n"
        )

        


