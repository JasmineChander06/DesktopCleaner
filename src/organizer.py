import os
import shutil
from pathlib import Path
from src.logger import logger
from src.backup import backup_file


def organize_desktop():

    desktop_path = str(Path.home() / "OneDrive" / "Desktop")

    files_by_ext = {}

    # Scan desktop and group files by extension
    for filename in os.listdir(desktop_path):

        file_path = os.path.join(desktop_path, filename)

        if os.path.isfile(file_path):

            ext = os.path.splitext(filename)[1].lower()

            if ext not in files_by_ext:
                files_by_ext[ext] = []

            files_by_ext[ext].append(file_path)

    # Create folders and move files
    for ext, paths in files_by_ext.items():

        folder_name = f"{ext[1:].upper()} Files"
        folder_path = os.path.join(desktop_path, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        for file_path in paths:

            try:
                #BACKUP BEFORE MOVING
                backup_file(file_path)

                # Move file after backup
                shutil.move(file_path, folder_path)

                logger.info(f"Moved {file_path} to {folder_path}")

            except Exception as e:
                logger.error(f"Error occurred while moving {file_path}: {e}")
