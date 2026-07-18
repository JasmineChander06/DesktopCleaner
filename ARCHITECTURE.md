1# Project Architecture

This document describes the internal architecture of the Desktop Organizer project, including 
module responsibilities, execution flow, folder structure, and design decisions. It provides a 
clear understanding of how the system works and how it can be extended

The Desktop Organizer is a modular Python application that scans the user's desktop, groups files by extension, creates categorized folders, backs up files, moves them, and logs all operations. The system is designed for safety, clarity, and extensibility.

The architecture follows a linear processing pipeline:

Scan → Group → Backup → Move → Log

This ensures that every file is handled consistently and safely.


2# Folder Structure

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

Explanation of Key Folders:

src/  
Contains all core modules. Each module has a single responsibility, following a clean separation-of-concerns design.

logs/  
Stores log files generated during execution. These logs record all file movements and errors.

backups/  
Stores daily backup folders containing copies of files before they are moved. This ensures data safety.

notebooks/  
Contains the original prototype and flowchart created during early development.



#3.Module Responsibilities

main.py
Entry point of the application.
Responsibilities:

Import and call organize_desktop() from src.organizer.

organizer.py
Core logic module.
Responsibilities:

Determine desktop path.

Scan files on the desktop.

Group files by extension.

Create destination folders.

Call backup before moving files.

Move files into categorized folders.

Log each operation.

>>backup.py
Handles backup operations.
Responsibilities:

Create date-based backup folders.

Copy files before moving them.

Ensure backups are stored safely for restoration.

>>logger.py
Configures logging.
Responsibilities:

Set log format and file location.

Provide a logger instance for use across modules.

Record both successful operations and errors.



#4.Execution Flow

>Step-by-Step Process

The user runs python main.py.

main.py calls organize_desktop() from src.organizer.

organizer.py determines the desktop path.

The desktop is scanned for files.

Files are grouped by extension.

For each file:

A backup is created using backup_file.

A destination folder is created if it does not exist.

The file is moved into the appropriate folder.

The operation is logged.


#5.Data Flow

>>Input:
Files located on the user's desktop.

Processing
File paths are read.

Extensions are extracted.

Backup copies are created.

Files are moved into categorized folders.

>>Output:
Organized folders on the desktop.

Backup copies in backups/<date>/.

Log entries in the logs directory.



#6.Design Decisions

Modular Design
Each module has a single responsibility, making the system easier to maintain, test, and extend.

Backup Before Move
Files are backed up before being moved to ensure data safety and allow restoration if needed.

Logging
Logs provide transparency, traceability, and debugging support.

Date-Based Backup Folders
Daily snapshots allow users to restore files from specific days.

Folder Naming Convention
Folders are named using the pattern <EXT> Files for clarity and consistency.

Jupyter Notebook Prototype
The notebook documents the initial logic, flowchart, and testing, demonstrating the evolution of the project.


#7.Future Architectural Extensions
Undo System (Not Yet Implemented)
A full restore mechanism using backups and logs.

Configuration File
Allow users to customize:

Desktop path

Folder names

Extension categories

Backup and logging settings

Command-Line Interface
Add flags such as:

--undo

--dry-run

--path <directory>

Graphical User Interface
A desktop interface for non-technical users using Tkinter or PyQt.

Scheduler Integration
Run the organizer automatically at intervals using system schedulers.

Advanced Logging
Separate logs by type or add more detailed information.

#8.Conclusion
The Desktop Organizer is built with clarity, safety, and extensibility in mind. Its modular architecture allows new features to be added without disrupting existing functionality, making it suitable for real-world use and future development.


