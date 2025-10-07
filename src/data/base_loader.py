# src/data/base_loader.py
import os
import zipfile
from pathlib import Path
import requests
from abc import ABC, abstractmethod

class BaseDatasetLoader(ABC):
    """
    Abstract base class for dataset downloaders and preprocessors.
    Each dataset subclass should implement its own URLs and preprocessing steps.
    """

    def __init__(self, output_folder: str = "data/raw", extract: bool = True):
        self.output_folder = Path(output_folder)
        self.extract = extract
        self.output_folder.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------
    # 🧩 Step 1: Download & Extract
    # ------------------------------------------------------
    def _download_file(self, url: str, dest_path: Path):
        """Download a file from a URL to a local path."""
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        if dest_path.exists():
            print(f"[INFO] {dest_path} already exists. Skipping download.")
            return

        print(f"[INFO] Downloading from {url} → {dest_path}")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(dest_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    def _extract_zip(self, zip_path: Path, extract_to: Path):
        """Extract a ZIP file safely."""
        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"[INFO] Extracted {zip_path.name} → {extract_to}")
            os.remove(zip_path)
        except zipfile.BadZipFile:
            print(f"[WARN] {zip_path} is not a valid zip file.")

    # ------------------------------------------------------
    # 🧩 Step 2: Abstract Methods (to override)
    # ------------------------------------------------------
    @abstractmethod
    def download(self):
        """Download raw data files."""
        pass

    @abstractmethod
    def preprocess(self):
        """Clean, standardize, and save to interim/processed folders."""
        pass

    # ------------------------------------------------------
    # 🧩 Step 3: Utility
    # ------------------------------------------------------
    def run_full_pipeline(self):
        """Run download → preprocess → ready-for-model pipeline."""
        print(f"[PIPELINE] Starting pipeline for {self.__class__.__name__}")
        self.download()
        self.preprocess()
        print(f"[PIPELINE] Completed pipeline for {self.__class__.__name__}")
