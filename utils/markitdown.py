from markitdown import MarkItDown
from utils import performance
import logging

logger = logging.getLogger(__name__)

OUTPUT_DIR = "markitdown"

@performance.execution_time
def convert_to_md(path):
    logger.info(f"Parsing doc {path} using markitdown")
    md = MarkItDown()
    result = md.convert(path)
    return result.text_content