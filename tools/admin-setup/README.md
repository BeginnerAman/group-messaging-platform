# Admin Setup Tool

This tool is a simple script that helps you choose who will be the administrator for your GroupChat app. It handles the secure password setup automatically so you do not have to write any code.

Running this script will replace all current administrators in the system with the new ones you enter.

## Requirements

You must have Python installed on your computer. Most computers have it already. If you do not have it, download it from the official python.org website and install it.

## Step by Step Guide for Beginners

### Step 1: Open the Terminal or Command Prompt

- On Windows: Press the Windows Key, type CMD, and press Enter to open the Command Prompt.
- On macOS: Press Command and Space, type Terminal, and press Enter.
- On Linux: Press Ctrl, Alt, and T keys together.

### Step 2: Navigate to this Directory

Type the following command in your terminal and press Enter:

cd tools/admin-setup

### Step 3: Run the Script

Type the following command and press Enter:

python setup_admins.py

If python does not work, try:

python3 setup_admins.py

### Step 4: Follow the On-Screen Prompts

- The script will ask you to type a username for the new administrator. Type it and press Enter.
- The script will ask you to type a password. Type it and press Enter. The password will be secured automatically.
- The script will ask if you want to add another administrator. Type y for yes, or n for no, and press Enter.

Once you are finished, the script will update the application files automatically. You can now test or deploy your app.
