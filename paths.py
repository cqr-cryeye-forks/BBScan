import pathlib
import os

ROOT_PATH = pathlib.Path(__file__).parent.absolute()
REPORT_FOLDER_PATH = ROOT_PATH.joinpath("report")

# Create the folder if it doesn't exist
if not os.path.exists(REPORT_FOLDER_PATH):
    os.makedirs(REPORT_FOLDER_PATH)
