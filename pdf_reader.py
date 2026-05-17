import fitz


def extract_pdf_text(file_path: str) -> str:
    page_texts = []

    with fitz.open(file_path) as doc:
        for page in doc:
            page_texts.append(page.get_text())

        return " ".join(page_texts)
