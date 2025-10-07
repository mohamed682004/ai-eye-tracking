from .base_loader import BaseDatasetLoader
from .helpers import data_loading_helpers as helpers
import h5py
import numpy as np
from pathlib import Path

class ZucoLoader(BaseDatasetLoader):
    """
    Loader for the ZuCo 2.0 EEG+Eye-tracking dataset.
    Handles extraction of word-level EEG and ET signals.
    """

    def __init__(self, output_folder="data/raw/ZuCo", extract=True):
        super().__init__(output_folder, extract)

    def download(self):
        # Optional — only if you want to auto-download from OSF
        print("[INFO] Please place ZuCo .mat files in", self.output_folder)

    def preprocess(self):
        data_dir = Path(self.output_folder)
        mat_files = list(data_dir.glob("*.mat"))

        all_sentences = []
        for file in mat_files:
            print(f"[INFO] Processing {file.name}")
            with h5py.File(file, "r") as f:
                # Each .mat contains subjects/sentences
                for sentence_key in f.keys():
                    sentence_data = f[sentence_key]
                    word_level_data = helpers.extract_word_level_data(
                        data_container=f,
                        word_objects=sentence_data,
                        eeg_float_resolution=np.float16
                    )
                    all_sentences.append(word_level_data)

        np.save(data_dir / "zuco_word_level.npy", all_sentences)
        print(f"[INFO] Saved standardized word-level data → {data_dir/'zuco_word_level.npy'}")
