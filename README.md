
---

# Warframe Screenshot Codex Reader and Inventory Manager

This project is a Python-based tool designed to help Warframe players efficiently manage their inventory and track progress. It uses OCR (Optical Character Recognition) to extract text from screenshots taken with a shortcut and organizes the extracted data into a CSV file for easy analysis.

## Features

1. **Quick Screenshot Capture**:
   - Press `Windows+Shift+S` to take a screenshot using the Windows Snipping Tool.
   - Automatically processes the image from the clipboard.

2. **OCR Text Extraction**:
   - Extracts text from screenshots using Tesseract OCR.
   - Dynamically organizes extracted text into rows and columns in a CSV file.

3. **Data Organization**:
   - Saves extracted text in a structured CSV file (`formatted_extracted_text.csv`).
   - Automatically adjusts rows and columns for better readability.

4. **Mastery Level Verification** *(Future Feature)*:
   - Compare extracted data with a database of Warframe items to check mastery level progress.

5. **Relic Scanner Enhancement** *(Future Feature)*:
   - Identify relics from screenshots for improved inventory management.

---

## Setup Instructions

### Prerequisites

1. **Python 3.8 or higher**: Ensure Python is installed on your system.
2. **Tesseract OCR**:
   - Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki).
   - Add Tesseract to your system's PATH during installation or manually configure it.

3. **Python Libraries**:
   Install required libraries using pip:
   ```bash
   pip install pytesseract pillow pandas keyboard
   ```

4. **Enable Clipboard History**:
   - Go to `Windows Settings > System > Clipboard` and enable "Clipboard History" to ensure screenshots are accessible from the clipboard.

---

### Installation

1. Clone or download this repository.
2. Save the provided Python script as `warframe_codex_reader.py` in your preferred directory.
3. Ensure Tesseract is installed and its path is correctly configured in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
   ```

---

## Usage

1. Run the script:
   ```bash
   python warframe_codex_reader.py
   ```

2. Use the `Windows+Shift+S` shortcut to take a screenshot of your Warframe inventory or codex.

3. The script will automatically:
   - Retrieve the screenshot from the clipboard.
   - Extract text using OCR.
   - Save the extracted data into `formatted_extracted_text.csv`.

4. Open `formatted_extracted_text.csv` in Excel or any spreadsheet tool to view organized data.

---

## Example Output

### Input Screenshot
The input screenshot shows Warframe inventory details, such as time, item names, stats, etc.

### Output CSV
| Timestamp | Item Name       | Stat 1 | Stat 2 | Time  |
|-----------|-----------------|--------|--------|-------|
| 15:27.2   | 2 ones          |        |        |       |
| ######### | B4 anubis Â     | 695    | 115    | 1.47s |

---

## Code Overview

### Main Components

#### 1. **ScreenshotOCR Class**
Handles the core functionality of capturing clipboard images, extracting text via Tesseract OCR, and saving data into a structured CSV file.

#### 2. **KeyboardListener Class**
Listens for the `Windows+Shift+S` shortcut and triggers the OCR process automatically.

#### 3. **CSV Formatting**
Uses `pandas` to dynamically adjust rows and columns for better organization of extracted data.

---

## Future Enhancements

1. **Mastery Level Verification**:
   - Import Warframe item data (e.g., weapons, frames) from an external database.
   - Compare extracted items with mastery progress to identify missing items.

2. **Relic Scanner**:
   - Enhance OCR capabilities to identify relics and their contents for better inventory management.

3. **GUI Integration**:
   - Add a graphical interface for easier interaction with the tool.

4. **Error Handling Improvements**:
   - Handle edge cases where no image is found in the clipboard or OCR fails due to poor image quality.

---

## Troubleshooting

1. **No Image Found in Clipboard**:
   - Ensure you use `Windows+Shift+S` and select an area before running the script.
   - Check that Clipboard History is enabled (`Windows Settings > System > Clipboard`).

2. **Tesseract Not Found**:
   - Verify that Tesseract is installed and its path is correctly set in the script:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
     ```

3. **Incorrect Text Extraction**:
   - Ensure the screenshot has clear text with good contrast.
   - Try adjusting Tesseract configurations (e.g., language settings).

---

## Contributing

Feel free to contribute by submitting pull requests or reporting issues on GitHub! Future improvements are welcome, especially for mastery level integration and relic scanning features.

---

## License

This project is licensed under the MIT License.

---
[1] https://pplx-res.cloudinary.com/image/upload/v1742653332/user_uploads/OooDkQWWqGikyQt/image.jpg

---
Answer from Perplexity: pplx.ai/share
