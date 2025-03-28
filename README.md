# Dev-Search

Dev-Search is a Django-based web application designed to help you **discover and connect with developers** from around the world. Whether you're looking for collaborators, seeking to expand your network, or simply exploring open-source projects, Dev-Search offers a user-friendly platform for developer search and interaction.

## Features

- **Developer & Project Search:** Browse and search for developers and projects with ease.
- **User Authentication:** Sign up, log in, and manage your account.
- **Profile Management:** Edit and update your developer profile.
- **Project Sharing:** Create, edit, and share your projects.
- **Messaging System:** Send messages to other developers and check your inbox.
- **Responsive Design:** Fully responsive UI built with Django templates, HTML, CSS, and JavaScript.

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (or SQLite for development)
- **Frontend:** HTML, CSS, JavaScript
- **Other:** Bootstrap (or custom CSS frameworks), Git

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vivek2540p/dev-search.git
   cd dev-search
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create a virtual environment
   python -m venv env

   # Activate the virtual environment on Windows
   env\Scripts\activate

   # On macOS/Linux, use:
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**

   - For development, the project is set up to use SQLite by default.
   - To switch to PostgreSQL, update your `DATABASES` setting in `settings.py` as shown below:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **(Optional) Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and visit [http://localhost:8000](http://localhost:8000) to view the application.

## Usage

Once the server is running, you can:
- **Browse Developers & Projects:** Use the search features on the homepage.
- **Manage Your Account:** Log in or sign up and update your profile.
- **Share Projects:** Post your own projects and view others’ work.
- **Messaging:** Use the messaging system to communicate with other developers.

## Contributing

Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to:
- **Project Maintainer:** [vivek2540p](https://github.com/vivek2540p)
- **Email:** vivekvaghasiya987@gmail.com

---

*Happy coding!*
