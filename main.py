import argparse
import logging
from os import listdir, mkdir, path
from os.path import isfile, join
from utils import docling, markitdown, performance

logger = logging.getLogger(__name__)

def process(input_dir, output_dir, lib):
    for f in listdir(input_dir):
        abs_path = join(input_dir, f)
        logger.info(f"Processing {abs_path}")
        if isfile(abs_path):
            logger.info("Is a file")
            converted_doc = lib.convert_to_md(abs_path)
            output_path = join(output_dir, lib.OUTPUT_DIR)
            if not path.isdir(output_path):
                mkdir(output_path)
            output_file = join(output_path, f"{f}.md")
            logger.info(output_file)
            with open(output_file, "w") as opf:
                opf.write(converted_doc)
        else:
            logger.info("Not a file")

def main():
    # Load all the args
    parser = argparse.ArgumentParser(description="Measure performance between docling and google enterprise ocr")
    parser.add_argument("--input_dir", help="Input directory", default="docs")
    parser.add_argument("--output_dir", help="Ouput directory", default="output")
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    process(input_dir, output_dir, docling)
    process(input_dir, output_dir, markitdown)

    performance.get_metrics()
   

if __name__ == "__main__":
    exit(main())
