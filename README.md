# gazzetExtractor1

# LLM Based Gazette Extractor

This project is specific for Sri Lankan Gazette Data Extraction. Mainly for Ministry/Department extra ordinary gazettes, amendments and People gazettes that assign Ministers, State Ministers, Deputy Ministers and Secretaries to ministries.

## Features

- Minister/Department gazette data extraction
- Amendment gazette data extraction
- Person gazette data extraction

## 🛠️ Installation

### Install as Package from GitHub
```bash
pip install git+https://github.com/Isuru-rangana/gazzetExtractor1.git
```

### For Linux Users (Alternative Installation)
If you encounter dependency issues, use the Linux-compatible requirements:
```bash
git clone https://github.com/Isuru-rangana/gazzetExtractor1.git
cd gazzetExtractor1
pip install -r requirements_linux.txt
pip install .
```

### Development Setup
#### Clone the repository
```bash
git clone https://github.com/Isuru-rangana/gazzetExtractor1.git
cd gazzetExtractor1
```
#### Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate     # On Windows
```
#### Install dependencies
```bash
pip install -r requirements_linux.txt  # For Linux
# OR
pip install -r requirements.txt        # For Windows
```

## 🚀 Usage

### Command Line Tool (After Installation)
```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# Extract ministry data
gztextractor --type ministry-initial --pdf path/to/gazette.pdf --output results/

# Extract person assignments
gztextractor --type persons --pdf path/to/gazette.pdf --output results/

# Extract amendments
gztextractor --type ministry-amendment --pdf path/to/gazette.pdf --output results/

# Extract amendment tables
gztextractor --type ministry-amendment-table --pdf path/to/gazette.pdf --output results/
```

### Python Library Usage
```python
from gztextractor import run_pipeline

# Set environment variable or pass API key
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'

# Extract data
result = run_pipeline(
    gazette_type="ministry-initial",
    pdf_path="path/to/gazette.pdf",
    output_path="results/"
)
print(result)
```

### Development Usage (Original Method)
#### Set environment variable
```bash
export OPENAI_API_KEY="your-api-key-here"
```
#### Run from source
```bash
python cli.py --type ministry-initial --pdf path_to_pdf --output output_directory

# Available types: ministry-initial, ministry-amendment, ministry-amendment-table, persons
# --pdf: path to the PDF file
# --output (optional): output directory, defaults to ./outputs/
```

## 📋 Supported Gazette Types

- `ministry-initial` - Initial ministry data extraction
- `ministry-amendment` - Ministry amendment data extraction  
- `ministry-amendment-table` - Amendment table data extraction
- `persons` - Personnel assignment data extraction

## 📁 Sample Files

The project includes sample gazette PDF files in the `assets/pdf/` directory for testing purposes.

## 🔧 Requirements

- Python 3.8+
- OpenAI API key
- Dependencies listed in `requirements.txt` (Windows) or `requirements_linux.txt` (Linux)
