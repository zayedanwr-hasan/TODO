# Todo List (Django)

Simple Django + Django REST Framework todo application with token-based authentication.

Quick setup (Windows)

1. Create & activate virtualenv:

   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run migrations:

   python manage.py makemigrations
   python manage.py migrate

   - If prompted for a default value when adding a non-nullable field, either provide a default or make the field nullable in `models.py`.

4. Create superuser:

   python manage.py createsuperuser

5. Run development server:

   python manage.py runserver

API Endpoints

- POST /api/register/  — register user (returns token)
- POST /api/token/     — obtain token
- /api/tasks/          — authenticated CRUD for tasks

Notes

- `Task` model fields: `owner`, `title`, `description`, `status`, `priority`, `complete`, `created_at`, `updated_at`.
- `owner` may be nullable to avoid migration issues with existing rows; you can make it non-null after handling data.

If you want, I can also generate migrations after your local verification.