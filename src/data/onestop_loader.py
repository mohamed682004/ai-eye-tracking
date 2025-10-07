# src/data/onestop_loader.py
from .base_loader import BaseDatasetLoader
from pathlib import Path

class OneStopLoader(BaseDatasetLoader):
    BASE_URL = "https://osf.io/download/"

    URLS = {
        "ordinary": {"fixations_Paragraph": "ne4az", "ia_Paragraph": "xkgfz"},
        "onestop": {"fixations_Paragraph": "dq935", "ia_Paragraph": "4ajc8"},
        # ... other modes if needed
    }

    def __init__(self, output_folder="data/raw/OneStop", mode="ordinary", extract=True):
        super().__init__(output_folder, extract)
        self.mode = mode

    def download(self):
        resources = self.URLS.get(self.mode)
        if resources is None:
            raise ValueError(f"Invalid mode: {self.mode}. Options: {list(self.URLS.keys())}")

        for name, code in resources.items():
            url = self.BASE_URL + code
            zip_path = self.output_folder / f"{self.mode}_{name}.zip"
            self._download_file(url, zip_path)
            if self.extract:
                self._extract_zip(zip_path, self.output_folder)

    def preprocess(self):
        """Later: implement CSV parsing, interpolation, normalization, etc."""
        print(f"[INFO] Preprocessing OneStop {self.mode} dataset...")
