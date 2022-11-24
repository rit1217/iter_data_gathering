import os
import logging


# Configure logging.
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
    force=True
)


# File configs.
TEMP_DIR = 'temp/'
BUNDLE_LIST = []
FILENAMES = {
    'raw_data_EN': 'raw_data_EN.json',
    'raw_data_TH': 'raw_data_TH.json',
    'missing_detail_EN': 'missing_detail_EN.json',
    'missing_detail_TH': 'missing_detail_TH.json'
}
FILEPATHS = {k: os.path.join(TEMP_DIR, v) for k, v in FILENAMES.items()}