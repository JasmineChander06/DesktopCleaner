Desktop Organizer

The Desktop Organizer is a modular Python automation tool designed to declutter and structure the user’s desktop by scanning files, grouping them by extension, creating categorized folders, backing up files, and logging all operations. The project began as a Jupyter Notebook prototype with a flowchart and evolved into a production-ready Python application with a clean architecture and extensible design.

This README provides a complete overview of the project, including its purpose, flowchart, architecture, module responsibilities, execution flow, and future enhancements.

>>#1. Problem Statement

Desktops often become cluttered with documents, images, downloads, temporary files, and miscellaneous items. This leads to:

Difficulty locating important files

No clear structure or categorization

Increased risk of accidental deletion

No traceability of changes

Manual organization is time-consuming and error-prone.
The Desktop Organizer automates this process safely and consistently.

>>2#Solution Overview
The Desktop Organizer solves the clutter problem by:

Scanning the desktop directory

Grouping files by extension

Creating categorized folders

Backing up files before moving

Moving files into their respective folders

Logging every action

This results in a clean, structured desktop with a safety net (backups) and full traceability (logs).

>>3#Flowchart (From Jupyter Notebook)

Below is the flowchart representing the logic implemented in the project:

Code
                ┌──────────────────────┐
                │     Start Program     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Scan Desktop Files   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Group by Extension    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Create Folder         │
                │ (e.g., TXT Files)     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     Backup File       │
                │ backups/YYYY-MM-DD/   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Move File to Folder   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     Log Operation     │
                │     logs/app.log      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │         End           │
                └──────────────────────┘

>>4#Features (Explained in Depth)

4.1 Automatic File Categorization
Scans the desktop using os.listdir and Path.home().

Extracts file extensions using os.path.splitext.

Groups files into extension-based categories.

Creates folders such as:

TXT Files

PDF Files

PNG Files

DOCX Files

Moves files into their respective folders using shutil.move.

This transforms a cluttered desktop into a structured workspace.

4.2 Backup System
Before moving any file, the organizer:

Creates a date-based folder inside backups/

Example:

Code
backups/
    2026-07-18/
        file1.txt
        file2.docx
Copies the original file into the backup folder using shutil.copy.

This ensures:

No file is lost

Files can be restored later

Daily snapshots of your desktop are preserved

4.3 Logging System
All operations are logged in:

Code
logs/app.log
Log entries include:

File moved

Folder created

Backup created

Errors (if any)

This provides full transparency and debugging support.

4.4 Modular Architecture
The project follows a clean, maintainable structure:

Code
src/
│ organizer.py
│ backup.py
│ logger.py
│ __init__.py
Each module has a single responsibility:

organizer.py → main logic

backup.py → backup system

logger.py → logging configuration

This makes the project easy to extend and debug.

4.5 Jupyter Notebook Prototype
The original prototype is stored in:

Code
notebooks/DesktopOrganiser.ipynb
It contains:

Early implementation

Flowchart

Testing

Visual explanation

This demonstrates the evolution from prototype to production code.

>>#5 Project Structure
Code
Desktop-Organizer/
│
├── main.py
├── README.md
├── ARCHITECTURE.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── organizer.py
│   ├── backup.py
│   ├── logger.py
│
├── logs/
├── backups/
│
└── notebooks/
    └── DesktopOrganiser.ipynb

>>#6 Installation

Clone the Repository
Code
git clone https://github.com/<your-username>/desktop-organizer.git
cd desktop-organizer
Install Dependencies
Code
pip install -r requirements.txt

>>#7 Usage
Run the organizer:

Code
python main.py
The script will:

Scan your desktop

Group files by extension

Create categorized folders

Back up files

Move files

Log everything

After running, you will see:

Organized folders on your desktop

Backups in backups/<date>/

Logs in logs/app.log


>>#8 How This Project Solves the Problem
This project provides:

Automation

Safety (backups)

Traceability (logs)

Structure (categorized folders)

Extensibility (modular design)

Instead of manually organizing files, users run a single command and the system handles everything.

>>#9 Future Enhancements
Undo System
Restore files from backups.

Configuration File
Custom folder names, paths, extension categories.

Command-Line Interface
Flags such as:

--undo

--dry-run

--path <directory>

GUI
Tkinter or PyQt interface.

Scheduler Integration
Automatic daily or weekly organization.

Advanced Logging
Separate logs by type.

