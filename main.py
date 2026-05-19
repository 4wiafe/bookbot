from pdf_reader import extract_pdf_text
from report import print_report
from stats import count_words, count_chars, sort_by_value


def main():
    book = "books/Wind_and_Truth.pdf"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

    extracted_text = extract_pdf_text(book)
    counted_words = count_words(extracted_text)
    counted_chars = count_chars(extracted_text)
    sorted_chars = sort_by_value(counted_chars)

    print_report(counted_words, sorted_chars)


if __name__ == "__main__":
    main()
