# PDF Text Annotation Extractor with Tesseract

## Description
This Python script is based on Allen AI's PAWLs project and is designed to perform OCR on PDF files to extract textual annotations present in each page. It leverages the pytesseract OCR engine. The output generated is aimed to be consistent across documents, making it ideal for machine learning training data, analytics, and other applications requiring standardized, high-quality text extraction.

While the PAWLs project offers a powerful preprocessor for handling PDFs, it is not actively maintained. Therefore, this separate project has been initiated to fill that gap and to continuously provide a reliable text extraction solution. Future updates plan to introduce additional preprocessors based on other underlying PDF engines.

## Requirements

- Python 3.9
- pytesseract
- pdf2image
- pandas

### Installation

Install the required Python packages using pip (from repo root):

```commandline
cd pdfpreprocessor
pip install .
```

## Development

Run linter (after install dependencies): 

```commandline
hatch run lint:fmt
```

## Usage

To run the script, simply call the `process_tesseract` function, passing in the PDF file's path as an argument:

\`\`\`python
from pdfprocessor.processor.tesseract import process_tesseract

annotations = process_tesseract("path/to/your/pdf/file.pdf")
\`\`\`

## Testing

Unit tests should be written to cover each of these functions. Testing can help ensure that the OCR extraction and scaling logic work as expected.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the Apache-2 License - see the `LICENSE.md` file for details.
