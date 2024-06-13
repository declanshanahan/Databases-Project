# Databases-Project

## Overview

This is a simple project management application built using Flask and SQLAlchemy. It allows users to add, edit, view, and delete projects. The application uses a PostgreSQL database to store project information.

## Features

- Home page
- Display a list of projects
- View project details
- Add a new project
- Edit an existing project
- Delete a project
- About page
- Contact page

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL

### Steps

1. Clone the repository or download the project files:
    ```bash
    git clone https://github.com/yourusername/project-management-app.git
    cd project-management-app
    ```

2. Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the PostgreSQL database:
   - Create a new PostgreSQL database named `flask_db`.
   - Update the `SQLALCHEMY_DATABASE_URI` in `app.py` if necessary.

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000`.


## Database Configuration

- The database configuration is set in `app.py` with the following line:

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://adm:root@localhost:5432/flask_db'
    ```

- Ensure that PostgreSQL is running and the database `flask_db` is created.

## Usage

- **Home Page:** The main landing page of the application.
- **Projects Page:** Lists all projects stored in the database. You can add a new project, view project details, edit a project, or delete a project from this page.
- **Project Details Page:** Displays detailed information about a specific project. Provides options to edit or delete the project.
- **Add Project Page:** A form to add a new project.
- **Edit Project Page:** A form to edit an existing project.
- **About Page:** Information about the application.
- **Contact Page:** Contact information.

## Deployment on Render.com

1. Create an account on Render.com and log in.
2. Create a new Web Service:
   - Connect your GitHub repository.
   - Select the repository containing your Flask application.
3. Set the Build Command to:
    ```bash
    pip install -r requirements.txt
    ```
4. Set the Start Command to:
    ```bash
    gunicorn app:app
    ```
5. Set up environment variables:
   - `DATABASE_URL` should be set to your PostgreSQL database URI.
6. Deploy the service.

## Links

- [GitHub Repository](https://github.com/xyz/flaskapp)
- [Deployed Application on Render.com](https://yourappname.onrender.com)

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
