# BookBot

BookBot is a simple Python project that analyzes a PDF book and generates a report showing:

- Total word count
- Character frequency (letters only)
- Characters sorted by frequency (descending)

It demonstrates basic text processing, file handling, and modular Python design.

---

## Features

- Extracts text from PDF files using PyMuPDF
- Counts total words in the text
- Counts occurrences of each alphabetic character
- Sorts characters by frequency
- Prints a clean formatted report

---

## How It Works

BookBot follows a simple pipeline:

1. Load PDF file
2. Extract text from the PDF
3. Count words in the text
4. Count character frequency
5. Sort characters by frequency
6. Print a formatted report

---

## Project Structure

```text
bookbot/
├── books/
│   └── Wind_and_Truth.pdf
├── pdf_reader.py
├── stats.py
├── report.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd bookbot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

---

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/Wind_and_Truth.pdf...
----------- Word Count ----------
Found 123,456 total words
--------- Character Count -------
e: 12,345
t: 9,876
a: 8,765
...
```

---

## Dependencies

- [PyMuPDF](https://pymupdf.readthedocs.io/) (imported as `fitz`) — PDF text extraction

---

## Tech Stack

- Python 3
- PyMuPDF
- Standard Python libraries

<hr />

Built as a learning project to practice:

- Python modules
- File handling
- Data structures
- Clean code architecture
