from docling.document_converter import DocumentConverter
from pathlib import Path
import logging
from utils import performance

logger = logging.getLogger(__name__)

OUTPUT_DIR = "docling"

@performance.execution_time
def convert_to_md(path):
    logger.info(f"Parsing doc {path} using docling")
    input_file_path = Path(path)
    converter = DocumentConverter()
    conversion_result = converter.convert(input_file_path)
    return conversion_result.document.export_to_markdown()
