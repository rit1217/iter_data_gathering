import argparse
import logging
from .get_raw_data import get_raw_data


log = logging.getLogger(__name__)


parser = argparse.ArgumentParser(description="TAT_raw_data CLI.")
parser.add_argument('-e', '--extract', action='store_true', help='Extract data.')
args = parser.parse_args()


if args.extract:
    log.info('Start extracting...')
    get_raw_data()


log.info('All done.')