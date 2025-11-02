from google.api_core.client_options import ClientOptions
from google.cloud import documentai_v1
import logging
from utils import performance

logger = logging.getLogger(__name__)

OUTPUT_DIR = "google"
PROJECT_ID = ""
PROCESSOR_ID = ""
LOCATION = ""

@performance.execution_time
def convert_to_md(file_path):
    # Set `api_endpoint` if you use a location other than "us".
    opts = ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")

    # Initialize Document AI client.
    client = documentai_v1.DocumentProcessorServiceClient(client_options=opts)

    # Get the Fully-qualified Processor path.
    full_processor_name = client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

    # Read the file into memory.
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Load binary data.
    # For supported MIME types, refer to https://cloud.google.com/document-ai/docs/file-types
    raw_document = documentai_v1.RawDocument(
        content=image_content,
        mime_type="application/pdf",
    )

    # Send a request and get the processed document.
    request = documentai_v1.ProcessRequest(name=full_processor_name, raw_document=raw_document)
    try:
        result = client.process_document(request=request)
        document = result.document
        return document.text
    except:
        logging.error(f"Could not parse {file_path}")
        return str("")