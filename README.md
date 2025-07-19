# Finance Tracker in Django

A web-based financial tracking application built with Django that helps users manage their personal finances, track expenses, and monitor their financial goals.

## Features

- User authentication and registration
- Dashboard with financial overview
- Expense tracking and categorization
- Account management
- Responsive design

## Technology Stack

- Python 3.13
- Django 5.2
- SQLite database
- HTML/CSS
- Bootstrap (for styling)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/arhamfareed106/finance-tracker-in-django.git
cd finance-tracker-in-django
```

2. Create and activate virtual environment:
```bash
python -m venv list
source list/Scripts/activate  # On Windows use: list\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

- `findj/` - Main project configuration
- `fintech/` - Main application directory
  - `templates/` - HTML templates
  - `models.py` - Database models
  - `views.py` - View logic
  - `urls.py` - URL configurations
  - `forms.py` - Form definitions

## Usage

1. Register a new account
2. Log in to your dashboard
3. Add and track your expenses
4. View financial summaries and reports

## License

This project is licensed under the MIT License.
