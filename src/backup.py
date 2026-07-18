import os
import shutil
from datetime import datetime


def backup_file(file_path):

    date_folder = datetime.now().strftime(
        "%Y-%m-%d"
    )

    backup_dir = os.path.join(
        "backups",
        date_folder
    )

    os.makedirs(
        backup_dir,
        exist_ok=True
    )

    shutil.copy2(
        file_path,
        backup_dir
    )