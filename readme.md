# GPT Metadata Generator

**Description:** In essence, this script automates the process of extracting specific metadata from a collection of PDF files (such as master theses) using the capabilities of the OpenAI API, and then stores this metadata in structured formats (CSV and XLSX) for further use or analysis.

**Authors** Maurice Vanderfeesten, in [collaboration with ChatGPT-4](https://chat.openai.com/share/83ac75e7-986f-4b4f-abb1-adc038fd1c92) 

![A machine with eight arms extract word-like particles  from a book in lab, and puts these words in a box.](./images/152940_A%20machine%20with%20eight%20arms%20extract%20word-like%20partic_xl-1024-v1-0.png)

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- `pip` (Python Package Installer)

### Installation & Setup

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/your_username/your_project_name.git
   cd your_project_name
   ```

2. **Set Up a Virtual Environment** (recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Rename `config-example.yaml` to `config.yaml`:

   ```bash
   mv configuration-example.yaml configuration.yaml  # On Windows use: rename configuration-example.yaml configuration.yaml
   ```

2. Open `configuration.yaml` in your preferred text editor. Update the various fields to match your setup and preferences. For example:

   - `openai_api_key`: Your OpenAI API key.
   - `input_directory`: Path to the directory containing input PDF files.
   - `results_directory`: Path where you'd like to save the results.
   - `max_tokens`: Maximum number of tokens for the OpenAI API response.

## Usage

Once everything is set up and configured, run the main script:

```bash
python main.py
```

This will process the PDF files as per the configurations and save the results in the specified directory.
