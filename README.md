
# Company Structure Django Project

## Description

This project is a Django web application that displays a hierarchical structure of company departments and employees. The application allows you to manage departments and employees through the Django admin panel. It also includes a function for generating mock data to demonstrate the application's functionality.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/uluk001/company_structure.git
   cd company_structure
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   Run migrations to create the necessary database tables:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   To access the Django admin panel, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. **Generate mock data:**

   Populate the database with sample data by running the script:

   ```bash
   python populate_db.py
   ```

7. **Run the development server:**

   After setting up the project, start the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Usage

1. **View the company structure:**

   Go to `http://127.0.0.1:8000/` to see the hierarchical structure of departments and employees.

2. **Admin panel:**

   To manage data, go to `http://127.0.0.1:8000/admin/` and log in with the superuser account.

## Project Structure

- `company_structure/` - The main Django project directory.
- `departments/` - The app for managing departments and employees.
- `populate_db.py` - Script for generating mock data.
- `templates/` - HTML templates for displaying the company structure.
- `static/` - Static files, including CSS and JavaScript for Bootstrap integration.

## Dependencies

The project uses the following libraries:

- Django 3.x
- Faker
- Bootstrap (via CDN)

## License

This project is licensed under the MIT License. For more details, see the LICENSE file.

## Contact

If you have any questions or suggestions regarding this project, please contact me at: ulukmanmuratov@gmail.com
