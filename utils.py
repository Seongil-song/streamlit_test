import base64
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

def get_base64_data(file):
    return base64.b64encode(file.read()).decode("utf-8")
