import streamlit as st
from PIL import Image
import utils

# Set up the main app
def main():
    st.title("Image OCR Web App")
    st.write("Upload an image and the app will perform OCR on it!")
    # st.sidebar.image('OIP.jpg',use_column_width=True)

    # Upload file
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")

        # On button click - perform OCR
        if st.button('Submit'):
            st.write("Performing OCR...")
            text = utils.ocr_core(image)
            st.write(text)

if __name__ == '__main__':
    main()
