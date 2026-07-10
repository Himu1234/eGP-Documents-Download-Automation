# eGP Documents Download Automation

## Overview

This project automates the process of downloading tender documents from the Bangladesh Electronic Government Procurement (e-GP) portal.

When evaluating a tender, committee members often need to download multiple documents submitted by different bidders under different forms. Doing this manually takes time because every document has to be opened and downloaded one by one.

This project performs those repetitive tasks automatically. It logs into the e-GP portal, searches for the required tender, collects the available forms and bidder information, creates an organized folder structure, and downloads all available documents into their respective folders.

The project was developed to save time, reduce repetitive manual work, and keep downloaded documents organized for future review and evaluation.

---

# Features

* Automatic login to the e-GP portal
* Search tender using Tender ID
* Open the Tender Dashboard automatically
* Read all available tender forms
* Read all participating bidders
* Create folders automatically
* Download documents for each bidder
* Save files in an organized folder structure
* Skip unavailable documents without stopping the program

---

# Project Structure

The project is divided into several small modules. Each module performs a specific task.

### `main.py`

This is the main program.

It controls the complete workflow by calling all other modules in the correct order.

---

### `config.py`

Stores project settings.

It reads information such as:

* e-GP username
* e-GP password
* Headless browser setting

The credentials are loaded from the `.env` file.

---

### `login.py`

Handles the login process.

It opens the browser, navigates to the e-GP portal, and signs in using the credentials provided in the `.env` file.

---

### `navigator.py`

Navigates through the e-GP portal after login.

It opens the required sections before searching for the tender.

---

### `search.py`

Searches for the required tender using the Tender ID and opens the Tender Dashboard.

---

### `opening.py`

Handles everything related to the **Opening** page.

Its responsibilities include:

* Reading available tender forms
* Reading bidder names
* Opening individual report pages
* Returning back to the Opening page after each download

---

### `folder_manager.py`

Creates the folder structure used to store downloaded documents.

Folders are automatically created based on the Tender ID, tender forms, and bidder names.

---

### `downloader.py`

Downloads the documents from the Individual Report pages and stores them in the correct folders.

---

### `selectors.py`

Contains page selectors used throughout the project.

Keeping selectors in a separate file makes the code easier to maintain if the e-GP website changes in the future.

---

### `.env`

Stores confidential information such as the e-GP username and password.

This file is not intended to be shared publicly.

---

# Folder Structure

After downloading, the folders will look similar to this:

```text
Tender_1296437
│
├── e-Tender Submission Letter
│   ├── Bidder A
│   ├── Bidder B
│   └── Bidder C
│
├── Tenderer Information Form
│   ├── Bidder A
│   ├── Bidder B
│   └── Bidder C
│
└── ...
```

This makes it easy to locate any document later.

---

# Requirements

Before running the project, make sure you have:

* Windows operating system
* Google Chrome installed
* Internet connection

Python does **not** need to be installed beforehand. Follow the instructions below.

---

# Installation

## Step 1 – Install Python

Download Python from:

https://www.python.org/downloads/

During installation, **make sure you check**

> **Add Python to PATH**

before clicking **Install Now**.

After installation, restart your computer if necessary.

---

## Step 2 – Download the Project

Either clone the repository

```bash
git clone https://github.com/Himu1234/eGP-Documents-Download-Automation.git
```

or download it as a ZIP file from GitHub and extract it.

---

## Step 3 – Open Command Prompt

Open the project folder.

Click the folder address bar, type

```text
cmd
```

and press **Enter**.

A Command Prompt window will open inside the project folder.

---

## Step 4 – Install Required Packages

Run the following commands one by one.

Install Playwright

```bash
pip install playwright
```

Install python-dotenv

```bash
pip install python-dotenv
```

Install the browser used by Playwright

```bash
playwright install
```

Wait until all installations finish.

---

## Step 5 – Configure the `.env` File

Open the `.env` file and enter your e-GP login information.

Example:

```text
EGP_USERNAME=your_username
EGP_PASSWORD=your_password
HEADLESS=False
```

If `HEADLESS=False`, you will be able to see the browser while the program is running.

If `HEADLESS=True`, the browser will run in the background.

---

## Step 6 – Set the Tender ID

Open `main.py`.

Find the following line:

```python
TENDER_ID = "1296437"
```

Replace the value with your required Tender ID.

Save the file.

---

## Step 7 – Run the Program

Run

```bash
python main.py
```

The browser will open automatically and the download process will begin.

---

# Common Problems

### "python is not recognized"

Python is either not installed or was installed without enabling **Add Python to PATH**.

Reinstall Python and make sure the checkbox is selected.

---

### "pip is not recognized"

Restart the computer after installing Python.

If the problem still exists, reinstall Python and enable **Add Python to PATH**.

---

### Browser does not open

Run

```bash
playwright install
```

again.

---

### Login fails

Check that the username and password in the `.env` file are correct.

---

# Disclaimer

This software is intended to automate repetitive document downloading from the Bangladesh e-GP portal. Users are responsible for ensuring that they use the software in accordance with the policies, regulations, and permissions of their organization and the e-GP system.
