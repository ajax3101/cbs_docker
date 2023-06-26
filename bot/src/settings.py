import logging
import os

from dotenv import load_dotenv

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.WARNING)
load_dotenv()

try:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
