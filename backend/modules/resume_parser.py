import PyPDF2
import docx

def parse_resume(file):

    filename = file.filename.lower()

    text = ""

    if filename.endswith(".pdf"):

        reader = PyPDF2.PdfReader(file.file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    elif filename.endswith(".docx"):

        document = docx.Document(file.file)

        for para in document.paragraphs:
            text += para.text + "\n"

    else:
        return "Unsupported file format"

    return text