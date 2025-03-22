import pytesseract
import pandas as pd
import keyboard
import logging
from PIL import ImageGrab
from datetime import datetime

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'

class ScreenshotOCR:
    def __init__(self, output_file='formatted_extracted_text.csv'):
        self.output_file = output_file
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def capture_clipboard_image(self):
        try:
            # Grab image from clipboard
            image = ImageGrab.grabclipboard()
            if isinstance(image, ImageGrab.Image.Image):
                return image
            else:
                self.logger.warning("No image found in clipboard. Ensure you've used Windows+Shift+S.")
                return None
        except Exception as e:
            self.logger.error(f"Error capturing clipboard image: {e}")
            return None

    def extract_text(self, image):
        try:
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            self.logger.error(f"Error extracting text: {e}")
            return ""

    def format_text_to_csv(self, text):
        try:
            # Split text into rows and columns dynamically
            rows = [line.split() for line in text.splitlines() if line.strip()]
            
            # Convert rows into a DataFrame for better organization
            df = pd.DataFrame(rows)
            
            # Replace None values with empty strings for clean formatting
            df = df.fillna('')
            
            # Save DataFrame to CSV file with proper formatting
            df.to_csv(self.output_file, index=False, header=False, encoding='utf-8')
            
            self.logger.info(f"Formatted data saved to {self.output_file}")
        except Exception as e:
            self.logger.error(f"Error formatting text to CSV: {e}")

    def process(self):
        clipboard_image = self.capture_clipboard_image()
        if clipboard_image:
            text = self.extract_text(clipboard_image)
            if text:
                self.format_text_to_csv(text)
                self.logger.info("Text extracted and formatted successfully!")
            else:
                self.logger.warning("No text extracted from clipboard image")
        else:
            self.logger.warning("Failed to retrieve image from clipboard")

class KeyboardListener:
    def __init__(self, ocr_processor):
        self.ocr_processor = ocr_processor

    def start(self):
        keyboard.add_hotkey('windows+shift+s', self.ocr_processor.process)
        keyboard.add_hotkey('shift+strg+c', self.ocr_processor.process)
        self.ocr_processor.logger.info("Keyboard listener started. Use Windows+Shift+S to take a screenshot and process it.")
        keyboard.wait()

def main():
    ocr_processor = ScreenshotOCR()
    listener = KeyboardListener(ocr_processor)
    listener.start()

if __name__ == "__main__":
    main()
