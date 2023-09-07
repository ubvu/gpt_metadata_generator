# GPT Metadata Generator

**Description:** In essence, this script automates the process of extracting specific metadata from a collection of PDF files (such as master theses) using the capabilities of the OpenAI API, and then stores this metadata in structured formats (CSV and XLSX) for further use or analysis.

**Authors** Maurice Vanderfeesten, in [collaboration with ChatGPT-4](https://chat.openai.com/share/83ac75e7-986f-4b4f-abb1-adc038fd1c92) 

![A friendly looking robot with eight arms extracts word-like particles from a book in a lab, and puts these word-like particles in a box next to it.](./images/438177_A%20friendly%20looking%20robot%20with%20eight%20arms%20extracts%20_xl-1024-v1-0.png)

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [git](https://git-scm.com/)
- [Python 3.x](https://www.python.org/)
- [`pip` (Python Package Installer)](https://pypi.org/project/pip/)

### Installation & Setup

1. **Clone the Repository**:
   
   ```bash
   git clone https://github.com/ubvu/gpt_metadata_generator.git
   cd gpt_metadata_generator
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
   mv config-example.yaml config.yaml  # On Windows use: rename config-example.yaml config.yaml
   ```

2. Open `config.yaml` in your preferred text editor. Update the various fields to match your setup and preferences. For example:

   - `openai_api_key`: Your OpenAI API key.
   - `input_directory`: Path to the directory containing input PDF files.
   - `results_directory`: Path where you'd like to save the results.
   - `max_tokens`: Maximum number of tokens for the OpenAI API response.
   - `MAX_TOKENS_FOR_CONTENT`: Setting a buffer size for the segments / chunk the pdf to ensure we don't feed the model too many tokens, exeeding its limit.
   - `model`: Setting the model to use default is "gpt-3.5-turbo" , include the quotes!

## Usage

Once everything is set up and configured, run the main script:

```bash
python main.py
```

This will process the PDF files as per the configurations and save the results in the specified directory.
