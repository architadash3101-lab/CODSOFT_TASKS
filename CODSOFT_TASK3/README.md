# Task 3: Image Captioning AI (CODSOFT AI Internship)

A beginner-friendly image captioning application built with Python, Streamlit, PyTorch, and Hugging Face Transformers. You upload a JPG, JPEG, or PNG image and the app generates a natural-language caption using the pretrained Salesforce/blip-image-captioning-base model.

Highlights:

- No API key, no paid service, and no camera required.
- Runs fully locally; the model is downloaded automatically on the first run.
- Automatically uses the GPU when CUDA is available, otherwise the CPU.

## Features

- Upload an image (JPG, JPEG, PNG) through a clean and professional Streamlit interface
- AI-generated natural-language caption using the pretrained BLIP model (no training needed)
- Automatic device selection: GPU (CUDA) when available, otherwise CPU
- Loading spinner while the caption is being generated
- Basic error handling for a smooth experience
- Model downloads itself on the first run, no manual setup

## Project Structure

    CODSOFT_TASKSNO/
    └── Task3_Image_Captioning/
        ├── app.py              Main Streamlit application
        ├── requirements.txt    Python dependencies
        ├── README.md           Installation and usage instructions (this file)
        └── .gitignore          Files ignored by Git

## Prerequisites

- Python 3.9 or newer (Python 3.10 or 3.11 is recommended)
- VS Code (recommended, but any editor or terminal works)
- Internet connection on the first run only, to download the model (about 1 GB)

## Installation and Usage

### 1. Open the project in VS Code

Open the Task3_Image_Captioning folder with VS Code (File > Open Folder), then open a terminal inside VS Code (Terminal > New Terminal).

### 2. Create and activate a virtual environment

It is recommended to use a virtual environment so the packages do not interfere with other Python projects.

Windows (Command Prompt or PowerShell):

    python -m venv .venv
    .venv\Scripts\activate

macOS or Linux:

    python3 -m venv .venv
    source .venv/bin/activate

After activation you should see (.venv) at the start of your terminal prompt.

### 3. Install the dependencies

    pip install -r requirements.txt

### 4. Run the application

    streamlit run app.py

Your browser will open automatically at http://localhost:8501. If it does not open by itself, copy that address into your browser manually.

## How to Use

1. Click Browse files and upload a JPG, JPEG, or PNG image.
2. The uploaded image appears on the page and a loading spinner is shown while the caption is generated.
3. The AI-generated caption is displayed clearly below the image.

Note: the first run downloads the BLIP model (about 1 GB) and can take a few minutes. On later runs the model is loaded from the local cache and everything is fast.

## Using a GPU (optional)

The app automatically uses CUDA/GPU when available. If you have an NVIDIA GPU, you can install the CUDA-enabled PyTorch build by following the instructions at https://pytorch.org/get-started/locally/ and the app will detect and use your GPU automatically. Without a GPU the app still works perfectly on the CPU, just a bit slower.

## How the Code Works

1. Streamlit shows the upload widget and the user interface.
2. Pillow (PIL) opens the uploaded image and converts it to RGB with Image.open(...).convert("RGB").
3. Hugging Face Transformers and PyTorch load the pretrained Salesforce/blip-image-captioning-base model.
4. The BLIP processor preprocesses the image and the model generates a caption with model.generate(...).
5. The caption is decoded with processor.decode(..., skip_special_tokens=True) and displayed on the page.

## Troubleshooting

- Port already in use: run streamlit run app.py --server.port 8502 instead.
- Caption generation is slow: this is normal on CPU. The first image also includes model loading time.
- Model download fails: check your internet connection and run the app again.
- Out of memory: close other applications and try again.
- If you delete the model cache folder (~/.cache/huggingface), the model will be downloaded again on the next run.

## Credits

- Application code: created for the CODSOFT Artificial Intelligence Internship (Task 3).
- Model: Salesforce/blip-image-captioning-base on Hugging Face. See the model card for license details: https://huggingface.co/Salesforce/blip-image-captioning-base
