# Quick Setup Guide

## Step-by-Step Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Database Migrations

```bash
python manage.py migrate
```

This will create the database file (`db.sqlite3`) and all necessary tables.

### 3. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account. You'll use this to log into the Django admin panel.

### 4. Verify Static Files

The images should already be in `static/assets/images/`. If not, copy them:

```bash
# On Windows (Git Bash)
cp -r assets/images/* static/assets/images/

# On Linux/Mac
cp -r assets/images/* static/assets/images/
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

### 7. Add Your First Scheme

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Click on **Schemes** under **WEBSITE**
4. Click **Add Scheme** button
5. Fill in the details:
   - **Name**: e.g., "50*20000(1000000)"
   - **Sala**: 1000000
   - **Instalments**: 50
   - **Auction Bid**: "25%"
   - **Period**: "Months"
   - **Instalment Amount**: 20000
   - **Auction Date**: "Every 9th day of the month"
   - **Header Color**: "gradient-primary" (or any CSS class)
   - **Coming Soon**: Unchecked (if all details are filled)
   - **Is Active**: Checked (to show on website)
6. Click **Save**
7. Visit http://127.0.0.1:8000/schemes/ to see your scheme!

## Common Header Color Options

- `gradient-primary` - Blue gradient (default)
- `bg-gradient-to-r from-green-500 to-emerald-600` - Green gradient
- `bg-gradient-to-r from-purple-500 to-pink-600` - Purple gradient
- `bg-gradient-to-r from-orange-500 to-amber-600` - Orange gradient
- `bg-gray-800` - Dark gray

## Troubleshooting

### Images Not Showing

Make sure images are in `static/assets/images/` and the server is running in DEBUG mode.

### Static Files Not Loading

Run:
```bash
python manage.py collectstatic
```

### Database Errors

Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3
python manage.py migrate
```

### Admin Panel Not Accessible

Make sure you created a superuser:
```bash
python manage.py createsuperuser
```

