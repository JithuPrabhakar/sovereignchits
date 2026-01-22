# Sovereign Chits - Django Application

A Django-based web application for Sovereign Chits Pvt Ltd, a chit fund company based in Kerala, India.

## Features

- **Django Admin Interface**: Manage chit fund schemes through Django admin panel
- **Dynamic Schemes Display**: Schemes added via admin are automatically displayed on the schemes page
- **Template-based Architecture**: All HTML pages converted to Django templates with a base template
- **Responsive Design**: Modern, mobile-friendly UI using Tailwind CSS

## Project Structure

```
sovereign-optimized/
├── manage.py
├── requirements.txt
├── db.sqlite3                  # SQLite database (created after migrations)
├── sovereign_chits/            # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── website/                    # Main Django app
│   ├── __init__.py
│   ├── admin.py                # Admin configuration for Scheme model
│   ├── apps.py
│   ├── models.py               # Scheme model
│   ├── views.py                # View functions
│   ├── urls.py                 # URL patterns
│   ├── templatetags/           # Custom template filters
│   │   ├── __init__.py
│   │   └── website_filters.py  # Custom intcomma filter
│   └── templates/
│       └── website/
│           ├── base.html       # Base template with common code
│           ├── index.html      # Home page
│           ├── about.html      # About page
│           ├── schemes.html    # Schemes listing page
│           └── contact.html    # Contact page
└── static/                     # Static files (CSS, JS, images)
    └── assets/
        └── images/             # All website images
```

**Note**: The old HTML files (`index.html`, `about.html`, `contact.html`, `schemes.html`, `admin-schemes.html`) and the `assets/` folder in the root directory have been removed as they are no longer needed. All images are now in `static/assets/images/`.

## Installation

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser** (to access Django admin):
   ```bash
   python manage.py createsuperuser
   ```

5. **Copy static files**:
   - Copy the `assets/images/` folder to `static/assets/images/`
   - Or run: `python manage.py collectstatic` (after configuring STATIC_ROOT)

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### Adding Schemes via Django Admin

1. Log in to the Django admin panel at `/admin/`
2. Navigate to **Website** → **Schemes**
3. Click **Add Scheme** to create a new scheme
4. Fill in the scheme details:
   - **Name**: Scheme name (e.g., "50*20000(1000000)")
   - **Sala**: Total sala amount in ₹
   - **Instalments**: Number of instalments
   - **Auction Bid**: Auction bid percentage or amount
   - **Period**: Period type (e.g., "Months", "Weeks")
   - **Instalment Amount**: Monthly instalment amount in ₹
   - **Auction Date**: Information about auction dates
   - **Header Color**: CSS class for header color (e.g., "gradient-primary", "bg-gradient-to-r from-blue-500 to-blue-700")
   - **Coming Soon**: Check if scheme details are incomplete
   - **Is Active**: Uncheck to hide from website
5. Click **Save** - the scheme will appear on the schemes page automatically

### Scheme Model Fields

- `name`: Scheme name
- `sala`: Total sala amount (Decimal)
- `instalments`: Number of instalments (Integer)
- `auction_bid`: Auction bid information (String)
- `period`: Period type (String)
- `instalment_amount`: Monthly instalment amount (Decimal)
- `auction_date`: Auction date information (Text)
- `header_color`: CSS class for header styling (String)
- `coming_soon`: Boolean flag for incomplete schemes
- `is_active`: Boolean flag to show/hide on website
- `created_at`: Auto-generated creation timestamp
- `updated_at`: Auto-generated update timestamp

## Pages

- **Home** (`/`): Landing page with company information
- **About** (`/about/`): About us page with company history, vision, and mission
- **Schemes** (`/schemes/`): Displays all active schemes from the database
- **Contact** (`/contact/`): Contact form and company information

## Template Structure

All templates extend `base.html` which contains:
- Common HTML structure
- Navigation bar
- Footer
- Common CSS styles
- Common JavaScript (mobile menu, year display)

Individual templates use Django template blocks:
- `{% block title %}`: Page title
- `{% block extra_css %}`: Page-specific CSS
- `{% block content %}`: Main page content
- `{% block extra_js %}`: Page-specific JavaScript

## Static Files

Static files (images, CSS, JS) should be placed in the `static/` directory:
- Images: `static/assets/images/`
- CSS: `static/css/` (if any custom CSS files)
- JS: `static/js/` (if any custom JS files)

## Development Notes

- The application uses SQLite database by default (for development)
- For production, update `settings.py` with appropriate database settings
- Update `SECRET_KEY` in `settings.py` for production
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` for production deployment

## License

© Sovereign Chits Pvt Ltd. All rights reserved.

