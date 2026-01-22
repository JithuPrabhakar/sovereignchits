# Deploying Sovereign Chits Django Application on GoDaddy

This guide will walk you through deploying your Django application on GoDaddy hosting.

## Prerequisites

- GoDaddy hosting account with cPanel access
- Python support enabled (GoDaddy shared hosting may have limitations)
- SSH access (if available)
- Domain name configured

## Important Considerations

⚠️ **Note**: GoDaddy shared hosting has limitations for Django applications:
- May not support Python/Django out of the box
- May require VPS or dedicated server for full Django support
- Consider alternatives like:
  - **PythonAnywhere** (Free tier available)
  - **Heroku** (Free tier available)
  - **DigitalOcean** (VPS starting at $4/month)
  - **AWS EC2** (Pay as you go)
  - **Railway** (Free tier available)

If GoDaddy doesn't support Django, we'll provide alternative deployment options.

## Option 1: GoDaddy with Python Support (If Available)

### Step 1: Prepare Your Application

1. **Update settings.py for production**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SECRET_KEY = 'your-production-secret-key-here'  # Generate a new one
   ```

2. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

3. **Create requirements.txt** (already exists):
   ```txt
   Django>=4.2.0,<5.0.0
   ```

### Step 2: Upload Files to GoDaddy

1. Log in to GoDaddy cPanel
2. Navigate to **File Manager**
3. Upload your project files to `public_html/` or a subdirectory
4. Ensure all files are uploaded including:
   - `manage.py`
   - `sovereign_chits/`
   - `website/`
   - `static/`
   - `requirements.txt`

### Step 3: Configure Python Environment

1. In cPanel, find **Python App** or **Setup Python App**
2. Create a new Python application
3. Set Python version (3.8 or higher)
4. Point to your project directory
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 4: Configure WSGI

1. Create or update `passenger_wsgi.py` in your project root:
   ```python
   import sys
   import os

   sys.path.insert(0, os.path.dirname(__file__))
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sovereign_chits.settings')

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

### Step 5: Database Setup

1. Create a MySQL database in cPanel
2. Update `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 7: Configure Static Files

1. Update `settings.py`:
   ```python
   STATIC_ROOT = '/home/username/public_html/staticfiles'
   STATIC_URL = '/static/'
   ```

2. Run collectstatic:
   ```bash
   python manage.py collectstatic
   ```

### Step 8: Set Permissions

```bash
chmod 755 manage.py
chmod -R 755 sovereign_chits/
chmod -R 755 website/
```

## Option 2: Alternative Hosting (Recommended)

### PythonAnywhere (Free Tier Available)

1. **Sign up**: https://www.pythonanywhere.com
2. **Upload files**: Use Files tab to upload your project
3. **Create web app**: 
   - Go to Web tab
   - Click "Add a new web app"
   - Choose Django
   - Select Python version
4. **Configure WSGI**:
   - Edit the WSGI file to point to your project
5. **Set up database**:
   - Use the built-in MySQL database
6. **Run migrations**:
   - Use the Bash console
7. **Collect static files**:
   - Configure static files mapping in Web tab

### Railway (Free Tier Available)

1. **Sign up**: https://railway.app
2. **Connect GitHub** (if using Git):
   - Push your code to GitHub
   - Connect repository to Railway
3. **Or upload directly**:
   - Create new project
   - Upload files
4. **Configure environment variables**:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS`
5. **Deploy**: Railway auto-detects Django and deploys

### Heroku (Free Tier Discontinued, Paid Options Available)

1. **Install Heroku CLI**
2. **Login**: `heroku login`
3. **Create app**: `heroku create your-app-name`
4. **Set config vars**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app.herokuapp.com
   ```
5. **Deploy**: `git push heroku main`
6. **Run migrations**: `heroku run python manage.py migrate`
7. **Create superuser**: `heroku run python manage.py createsuperuser`

## Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Generate new `SECRET_KEY`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Configure production database
- [ ] Set up static files serving
- [ ] Configure media files (if needed)
- [ ] Set up SSL certificate (HTTPS)
- [ ] Configure domain name
- [ ] Set up backups
- [ ] Configure error logging
- [ ] Test all functionality
- [ ] Create admin superuser

## Security Recommendations

1. **Never commit SECRET_KEY** to version control
2. **Use environment variables** for sensitive data
3. **Enable HTTPS** (SSL certificate)
4. **Regular backups** of database
5. **Keep Django updated** for security patches
6. **Use strong passwords** for admin accounts
7. **Limit admin access** to trusted users only

## Troubleshooting

### Static files not loading
- Check `STATIC_ROOT` and `STATIC_URL` settings
- Run `collectstatic` command
- Verify file permissions

### Database connection errors
- Check database credentials
- Verify database exists
- Check host and port settings

### 500 Internal Server Error
- Check error logs in cPanel
- Verify `DEBUG = False` and check error pages
- Review Django logs

### Admin panel not accessible
- Verify superuser exists
- Check URL configuration
- Verify admin is enabled in `INSTALLED_APPS`

## Support

For GoDaddy-specific issues, contact GoDaddy support.
For Django deployment issues, refer to Django deployment documentation: https://docs.djangoproject.com/en/stable/howto/deployment/

## Recommended Next Steps

1. **Choose hosting platform** based on your needs
2. **Set up staging environment** for testing
3. **Configure domain name** DNS settings
4. **Set up automated backups**
5. **Monitor application** performance
6. **Set up error tracking** (e.g., Sentry)

