# Django Project Setup Guide

Welcome!  
Follow these instructions to set up and run the project on your local machine.

---

## Requirements

- Python 3.9 or higher (recommended: 3.10)
- pip (Python package installer)
- virtualenv (recommended)
- PostgreSQL or SQLite (depending on project settings)

---

## 1. Extract the ZIP File

- **Windows**: Right-click the `.zip` → "Extract All" → choose a location.
- **Mac**: Double-click the `.zip` → it will extract into a folder.

---

## 2. Open Terminal or Command Prompt

- **Windows**: Press `Win + R`, type `cmd`, and press Enter.
- **Mac**: Open `Terminal` from `Applications > Utilities > Terminal`.

---

## 3. Navigate to the Project Directory

```bash
cd path/to/your/project

---

🛠️ 4. Create and Activate a Virtual Environment
Windows
 - python -m venv env
 - env\Scripts\activate
Mac/Linux
 - python3 -m venv env
 - source env/bin/activate

⚡ Tip: If venv is not available, install it using:
    pip install virtualenv

📦 5. Install Project Dependencies
    - pip install -r requirements.txt

🗄️ 6. Apply Database Migrations
    - python manage.py migrate

   7. Running in Development Mode
        - To start Django Tailwind in development mode, run the following command in a terminal:

        - python manage.py tailwind start


🚀 8. Run the Development Server
    - python manage.py runserver
# touched on 2025-05-27T15:28:53.856785Z
# touched on 2025-05-27T15:29:13.442689Z
# touched on 2025-07-09T21:54:14.004458Z
# touched on 2025-07-09T21:54:18.512712Z
# touched on 2025-07-09T21:54:30.474882Z
# touched on 2025-07-09T21:55:04.332418Z
# touched on 2025-07-09T21:55:15.311758Z
# touched on 2025-07-09T21:55:17.993553Z
# touched on 2025-07-09T21:55:21.739444Z
# touched on 2025-07-09T21:55:41.754345Z
# touched on 2025-07-09T21:56:10.106020Z
# touched on 2025-07-09T21:56:26.175777Z
# touched on 2025-07-09T21:56:31.254518Z
# touched on 2025-07-09T21:56:56.671971Z
# touched on 2025-07-09T21:57:08.212209Z
# touched on 2025-07-09T21:57:25.207973Z
# touched on 2025-07-09T21:57:42.819140Z
# touched on 2025-07-09T21:57:58.235630Z