import openai
import PyPDF2
import pandas as pd
import os
import yaml

# Load configurations from config.yaml
with open("config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize OpenAI API with your key
openai.api_key = config['openai_api_key']

# Extract text from the PDF
def extract_pdf_content(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        content = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            content += page.extract_text()
    return content

# Input directory containing PDF files
input_directory = config['input_directory']

# List all PDF files in the directory
pdf_files = [file for file in os.listdir(input_directory) if file.endswith('.pdf')]

# DataFrame to store all metadata
all_metadata = pd.DataFrame(columns=["File Name", "Metadata Field", "Value"])

# Loop through each PDF file and process
for pdf_file in pdf_files:
    pdf_content = extract_pdf_content(os.path.join(input_directory, pdf_file))
    
    # Define a function to segment the text into chunks
    def segment_text(text, max_tokens):
        words = text.split()
        segments = []
        current_segment = []

        current_token_count = 0
        for word in words:
            if current_token_count + len(word.split()) <= max_tokens:
                current_segment.append(word)
                current_token_count += len(word.split())
            else:
                segments.append(" ".join(current_segment))
                current_segment = [word]
                current_token_count = len(word.split())

        if current_segment:
            segments.append(" ".join(current_segment))

        return segments

    # Segment the PDF content into chunks
    MAX_TOKENS_FOR_CONTENT = config['MAX_TOKENS_FOR_CONTENT']
    segments = segment_text(pdf_content, MAX_TOKENS_FOR_CONTENT)

    all_metadata_fields = []

    # Process each segment
    for segment in segments:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"""
            Please extract the following Dublin Core Metadata fields from the provided text:
            - Title
            - Creator (Author)
            - Date
            - Type
            - Identifier (DOI)
            - Publisher
            - Rights
            - Language
            - Format
            - Source
            - Relation
            - Coverage
            Text: {segment}
            """}
        ]

        response = openai.ChatCompletion.create(
            model=config['model'],
            messages=messages
        )

        metadata_fields = response.choices[0].message['content'].strip().split("\n")
        all_metadata_fields.extend(metadata_fields)

    # Process the combined results from all segments   
    # Convert metadata fields to DataFrame and append to all_metadata
    df = pd.DataFrame(all_metadata_fields, columns=["Metadata Field", "Value"])
    df.insert(0, "File Name", pdf_file)
    all_metadata = all_metadata.append(df, ignore_index=True)

# Create "results" directory if it doesn't exist
results_directory = config['results_directory']
if not os.path.exists(results_directory):
    os.makedirs(results_directory)

# Export to CSV and XLSX in the "results" directory
csv_path = os.path.join(results_directory, "metadata.csv")
xlsx_path = os.path.join(results_directory, "metadata.xlsx")
all_metadata.to_csv(csv_path, index=False)
all_metadata.to_excel(xlsx_path, index=False)

csv_path, xlsx_path