BugHub - CS50W Final Project

Distinctiveness and Complexity:
BugHub is a simple, efficient platform that lets security researchers report bugs directly to companies. It is clearly distinct from previous CS50W projects because it is neither a social network nor an e-commerce platform. It stands out by offering a straightforward way for security researchers to report vulnerabilities directly to companies, who can manage these reports, accept or reject them, and maintain clear communication.

The complexity of the project arises from the implementation of multiple user roles (Researchers, Companies, Admins) using a custom Django user model (AbstractUser). Each role has specific functionalities:
- Researchers can create aAnd track their own reports.
- Companies can review these reports and manage their status.
- Admins can manage users and track all activities.

Moreover, the project meets the JavaScript requirement by having a simple character-counting feature when researchers fill in bug descriptions. The UI is responsive and designed with Bootstrap, using a clean theme of blue, sky blue, black, and white.

Distinctiveness and Complexity
- Custom User Roles: Implemented via a custom Django User model, distinguishing clearly between researchers, companies, and admins.
- Bug Reporting Workflow: Researchers can report vulnerabilities directly linked to specific companies. Companies can review, accept, reject, and resolve these reports.
- Simple JavaScript: Real-time character counting enhances user experience when reporting bugs.
- Role-Based Dashboards: Users are redirected to specific dashboards based on their role after login.

Project Structure
- models.py: Defines User, Bug, Comments, and AuditLog models.
- views.py: Contains all logic for authentication, dashboard views for each role, and bug-report handling.
- forms.py: Defines SignupForm and BugForm for bug submissions and user registrations.
- urls.py: Manages URL routing throughout the application.
- templates/registration/: HTML files for authentication (login, signup).
- templates/reports/: HTML files structured for each user role (dashboards, bug submission).
- static/reports/style.css: Custom CSS for design enhancements.
- static/reports/script.js: JavaScript for character counting feature.

How to Run the Application
1. Clone this repository.
2. Ensure Python and Django are installed.
3. Run the following commands:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

4. Access the application at http://127.0.0.1:8000.

Additional Information
- Django built-in authentication used (login, signup, logout).
- All static files (CSS, JS) correctly placed under the static/reports directory.

This project was intentionally kept simple yet functional to fulfill the requirements for CS50W certification efficiently.

Dependencies
All dependencies are standard Django packages. For convenience:
Django

Video Demonstration
A short video demonstrating the project features will be submitted separately according to CS50W instructions.

Thanks for reviewing my project!

