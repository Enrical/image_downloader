# Image Downloader Web App

A simple and intuitive web app built with **Streamlit** to download images from URLs listed in an Excel file. This app lets users upload an Excel file, select the columns for image URLs and filenames, and download the images as a compressed ZIP file.

## Features

- **Upload Excel Files**: Supports `.xlsx` format.
- **Dynamic Column Selection**: Select columns for image URLs and filenames using an easy-to-use interface.
- **On-Demand Download**: Images are downloaded only after clicking the "Download Images" button.
- **Compressed Output**: All downloaded images are packaged into a single ZIP file for easy access.
- **Error Handling**: Handles invalid links, missing columns, and other potential issues gracefully.

## Demo

![Demo Screenshot](demo_screenshot.png) *(Optional: Add a screenshot of the app in action)*

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` installed

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-downloader.git
   cd image-downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open the link provided by Streamlit (e.g., `http://localhost:8501`) in your browser.

## Usage

1. Upload an Excel file containing:
   - A column with image URLs.
   - A column with filenames to name the downloaded images.
2. Select the appropriate columns for URLs and filenames.
3. Click "Download Images" to fetch the images.
4. Once completed, download the ZIP file containing all the images.

## Example Excel File

| Links                          | Applicant Name |
|--------------------------------|----------------|
| https://example.com/image1.jpg | John Doe       |
| https://example.com/image2.jpg | Jane Smith     |

## Deployment

To deploy this app online (e.g., on Streamlit Cloud):

1. Push this project to a GitHub repository.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud).
3. Create a new app and link it to your repository.
4. Configure the `requirements.txt` file to install necessary dependencies automatically.

## Dependencies

- `streamlit`
- `pandas`
- `requests`
- `openpyxl`

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

You can customize this further by adding a demo GIF or screenshot, deployment URL (if hosted), and your contact information. Let me know if you'd like help with any additional customization!
