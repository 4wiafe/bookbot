from pdf_reader import extract_pdf_text


def count_words(text: str) -> int:
    return len(text.split())
