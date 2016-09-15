import zipfile
import argparse

def extract(zip_file_location, where_to_extract):
    with zipfile.ZipFile(zip_file_location, "r") as z:
        z.extractall(where_to_extract)

parser = argparse.ArgumentParser()
parser.add_argument('-z', help='zip file location')
parser.add_argument('-d', help='where to extract')
args = parser.parse_args()

extract(args.z, args.d)
