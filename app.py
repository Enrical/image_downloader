import pandas as pd
import requests
import os
import shutil
import streamlit as st

# Streamlit app
def main():
    st.title("Image Downloader")
    st.write("Upload an Excel file with image links and filenames to download images.")

    # Step 1: Upload the Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type=['xlsx'])
    if uploaded_file is not None:
        try:
            # Step 2: Read the Excel file
            data = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Error reading Excel file: {e}")
            return

        # Display the dataframe for user reference
        st.write("Preview of the uploaded Excel file:")
        st.dataframe(data.head())

        # Step 3: Allow user to select columns
        st.write("Select the columns containing the image URLs and filenames:")
        url_column = st.selectbox("Select the column for image URLs:", data.columns)
        name_column = st.selectbox("Select the column for filenames:", data.columns)

        # Add a button to confirm and start the download process
        if st.button("Download Images"):
            if not url_column or not name_column:
                st.error("Please select both columns to proceed.")
                return

            # Step 4: Create the output folder
            output_folder = 'downloaded_images'
            os.makedirs(output_folder, exist_ok=True)

            # Step 5: Download the images
            st.write("Starting image downloads...")
            for idx, row in data.iterrows():
                link = row[url_column]
                name = row[name_column]
                # Clean the name to make it a valid filename
                cleaned_name = ''.join(c for c in name if c.isalnum() or c in " _-").strip()
                file_path = os.path.join(output_folder, f'{cleaned_name}.jpg')  # Adjust extension if needed

                try:
                    response = requests.get(link, stream=True)
                    if response.status_code == 200:
                        # Save the image
                        with open(file_path, 'wb') as file:
                            for chunk in response.iter_content(1024):
                                file.write(chunk)
                        st.write(f"Downloaded: {cleaned_name}.jpg")
                    else:
                        st.warning(f"Failed to download {link} - Status Code: {response.status_code}")
                except Exception as e:
                    st.error(f"Error downloading {link}: {e}")

            # Step 6: Compress the images into a ZIP file
            zip_file_name = 'downloaded_images.zip'
            shutil.make_archive('downloaded_images', 'zip', output_folder)
            st.success("All images downloaded and compressed into a ZIP file.")

            # Step 7: Provide the ZIP file for download
            with open(zip_file_name, 'rb') as zip_file:
                st.download_button(
                    label="Download ZIP File",
                    data=zip_file,
                    file_name=zip_file_name,
                    mime='application/zip'
                )

if __name__ == "__main__":
    main()
