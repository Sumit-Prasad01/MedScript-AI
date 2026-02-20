import requests
import os
from pathlib import Path
from app.common.logger import get_logger
from app.config.config import Paths

logger = get_logger(__name__)

class PDFDownloader:
    def __init__(self, target_folder):
        self.target_folder = Path(target_folder)
        self._prepare_directory()

    def _prepare_directory(self):
        """Creates the destination folder if it doesn't exist."""
        if not self.target_folder.exists():
            self.target_folder.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {self.target_folder}")

    def download_pdf(self, url, filename):
        """Downloads a PDF from a raw URL and saves it locally."""
        save_path = self.target_folder / filename
        
        raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
        
        try:
            logger.info(f"Initiating download from: {raw_url}")
            response = requests.get(raw_url, stream=True)
            response.raise_for_status()  

            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            logger.info(f"Success! File saved to: {save_path}")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to download file: {e}")
            return False

if __name__ == "__main__":

    downloader = PDFDownloader(Paths.DATA_DIR)
    downloader.download_pdf(Paths.GITHUB_URL, Paths.FILE_NAME)