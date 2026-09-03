# Task 3: Image Captioning AI
# CODSOFT Artificial Intelligence Internship
#
# A beginner-friendly Streamlit app that generates a natural-language
# caption for an uploaded image using the pretrained BLIP model
# (Salesforce/blip-image-captioning-base) from Hugging Face.
#
# Run with:  streamlit run app.py

import streamlit as st
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

MODEL_NAME = "Salesforce/blip-image-captioning-base"


@st.cache_resource(show_spinner=False)
def load_model_and_processor():
    """Download (on first run) and load the BLIP model and its processor.

    The result is cached by Streamlit, so the model is loaded only once
    per app session, which keeps things fast after the first run.
    """
    # Use the GPU automatically when CUDA is available, otherwise the CPU.
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    processor = BlipProcessor.from_pretrained(MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

    return processor, model, device


st.set_page_config(
    page_title="Image Captioning AI",
    page_icon=":frame_with_picture:",
    layout="centered",
)

st.title(":frame_with_picture: Image Captioning AI")
st.markdown(
    "Upload an image (JPG, JPEG, or PNG) and the app will generate a "
    "natural-language caption for it using a pretrained BLIP model."
)

with st.sidebar:
    st.header("About")
    st.info(
        "This app runs fully on your machine.\n\n"
        "No API key is required. The model is downloaded automatically "
        "the first time the app runs (about 1 GB)."
    )
    device_name = "GPU (CUDA)" if torch.cuda.is_available() else "CPU"
    st.caption(f"Processing device: {device_name}")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG, PNG",
)

if uploaded_file is not None:
    # Open and display the uploaded image
    try:
        # convert("RGB") makes sure the image has 3 colour channels,
        # which is what the BLIP model expects.
        image = Image.open(uploaded_file).convert("RGB")
    except Exception as e:
        st.error(f"Sorry, the file could not be opened as an image. {e}")
        st.stop()

    st.image(image, caption="Your uploaded image", use_container_width=True)

    if st.button(":sparkles: Generate Caption", type="primary"):
        # Load the model (this is fast on later runs thanks to the cache)
        try:
            with st.spinner("Loading the model... the first run can take a few minutes."):
                processor, model, device = load_model_and_processor()
        except Exception as e:
            st.error(
                "The model could not be loaded. Please check your internet "
                f"connection and try again.\n\n{e}"
            )
            st.stop()

        # Generate the caption
        try:
            with st.spinner("Generating caption..."):
                inputs = processor(images=image, return_tensors="pt").to(device)
                generated_ids = model.generate(**inputs)
                caption = processor.decode(generated_ids[0], skip_special_tokens=True)
        except Exception as e:
            st.error(f"Something went wrong while generating the caption. {e}")
            st.stop()

        st.subheader("Generated Caption")
        st.success(caption)

with st.expander("How it works"):
    st.markdown(
        "1. The uploaded image is opened with Pillow and converted to RGB.\n"
        "2. BlipProcessor preprocesses the image for the BLIP model.\n"
        "3. BlipForConditionalGeneration creates the caption with model.generate(...).\n"
        "4. The caption is decoded and displayed on the page."
    )
