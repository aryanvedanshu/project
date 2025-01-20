import PyPDF2
import re

def extract_questions_from_pdf(pdf_path, output_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = pdf_reader.numPages

        for page_num in range(total_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extract_text()

            # Define a regular expression to identify questions
            question_pattern = re.compile(r'\bQuestion [0-9]+[.:]')

            # Use the regular expression to find matches
            matches = question_pattern.split(text)

            # Filter out empty strings and remove leading/trailing whitespaces
            questions = [match.strip() for match in matches if match.strip()]

            # Write each question to a new file
            for i, question in enumerate(questions):
                output_file_path = f"{output_path}/question_{page_num + 1}_{i + 1}.txt"
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(question)

if __name__ == "__main__":
    pdf_path = "path/to/your/file.pdf"
    output_path = "path/to/output/directory"

    extract_questions_from_pdf(pdf_path, output_path)
