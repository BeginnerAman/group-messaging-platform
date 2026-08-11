# Admin Setup Tool

This tool is a Python script that helps you configure the administrators for GroupChat. It prompts you for administrator names and passwords, automatically hashes the passwords using SHA-256, and writes them directly to app.js.

Any previous administrators in the code will be deleted and replaced by the new administrators you enter.

## Requirements

- Python 3.x

## How to Run

1. Open your command line or terminal.
2. Navigate to this directory:
   cd tools/admin-setup
3. Run the Python script:
   python setup_admins.py
4. Follow the interactive prompts to add as many administrators as you want.
5. After completing the setup, deploy or test the updated files.
