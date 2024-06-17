from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://adm:root@localhost:5432/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Project {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Home page route."""
    return render_template('home.html')

@app.route('/projects')
def projects():
    """Route to display all projects."""
    all_projects = Project.query.all()
    return render_template('projects.html', projects=all_projects)

@app.route('/project/<int:project_id>')
def project_details(project_id):
    """Route to display details of a specific project."""
    project = Project.query.get_or_404(project_id)
    return render_template('project_details.html', project=project)

@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    """Route to add a new project."""
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_project = Project(name=name, description=description)
        try:
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for('projects'))
        except Exception as e:
            return f"An error occurred while adding the project: {e}"
    return render_template('add_project.html')

@app.route('/edit_project/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    """Route to edit an existing project."""
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        project.name = request.form['name']
        project.description = request.form['description']
        try:
            db.session.commit()
            return redirect(url_for('projects'))
        except Exception as e:
            return f"An error occurred while editing the project: {e}"
    return render_template('edit_project.html', project=project)

@app.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    """Route to delete a project."""
    project = Project.query.get_or_404(project_id)
    try:
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for('projects'))
    except Exception as e:
        return f"An error occurred while deleting the project: {e}"

if __name__ == '__main__':
    app.run(debug=True)
