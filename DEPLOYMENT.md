# Deployment Guide

## Production Deployment Options

### 1. Heroku Deployment

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Steps
```bash
# Login to Heroku
heroku login

# Create new app
heroku create plantsecure-app

# Add buildpack
heroku buildpacks:set heroku/python

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set ELEVENLABS_API_KEY="your-key"
heroku config:set OPENWEATHER_API_KEY="your-key"

# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Push to Heroku
git push heroku main

# Run migrations
heroku run python
```

#### Heroku Configuration Files

**Procfile:**
```
web: gunicorn app:app --chdir App
```

**runtime.txt:**
```
python-3.10.11
```

### 2. AWS EC2 Deployment

#### Setup
```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-instance-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx -y

# Clone repository
git clone https://github.com/Benkmsn/Plantsecure_Plant-Disease-Detection.git
cd Plantsecure_Plant-Disease-Detection/App

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup Gunicorn
pip install gunicorn

# Create systemd service
sudo nano /etc/systemd/system/plantsecure.service
```

**plantsecure.service:**
```ini
[Unit]
Description=PlantSecure Flask App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/Plantsecure_Plant-Disease-Detection/App
Environment="PATH=/home/ubuntu/Plantsecure_Plant-Disease-Detection/App/venv/bin"
ExecStart=/home/ubuntu/Plantsecure_Plant-Disease-Detection/App/venv/bin/gunicorn -w 4 -b 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```

#### Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /home/ubuntu/Plantsecure_Plant-Disease-Detection/App/static;
    }
}
```

### 3. Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY App/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY App/ .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - ELEVENLABS_API_KEY=${ELEVENLABS_API_KEY}
      - OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}
    volumes:
      - ./App/static/uploads:/app/static/uploads
      - ./App/instance:/app/instance
```

**Build and Run:**
```bash
docker-compose up -d
```

### 4. Railway Deployment

1. Push code to GitHub
2. Go to [Railway.app](https://railway.app)
3. Click "New Project" > "Deploy from GitHub"
4. Select your repository
5. Add environment variables
6. Deploy!

### 5. PythonAnywhere Deployment

1. Create account at [PythonAnywhere](https://www.pythonanywhere.com)
2. Open Bash console
3. Clone repository
4. Create virtual environment
5. Install dependencies
6. Configure Web app in dashboard
7. Set WSGI file

## Production Checklist

- [ ] Set `FLASK_ENV=production`
- [ ] Set `FLASK_DEBUG=False`
- [ ] Use production database (PostgreSQL/MySQL)
- [ ] Enable HTTPS/SSL
- [ ] Set up CDN for static files
- [ ] Configure email service
- [ ] Set up logging and monitoring
- [ ] Add rate limiting
- [ ] Configure backup strategy
- [ ] Set up error tracking (Sentry)
- [ ] Enable auto-scaling
- [ ] Configure domain name
- [ ] Set up CI/CD pipeline

## Database Migration to Production

### PostgreSQL Setup
```python
# Update app.py
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Install psycopg2
pip install psycopg2-binary

# Create tables
python
>>> from app import db
>>> db.create_all()
```

## Environment Variables for Production

Required:
```
SECRET_KEY=<long-random-string>
ELEVENLABS_API_KEY=<your-key>
OPENWEATHER_API_KEY=<your-key>
DATABASE_URL=<production-db-url>
FLASK_ENV=production
```

Optional:
```
SENTRY_DSN=<for-error-tracking>
REDIS_URL=<for-caching>
EMAIL_HOST=<smtp-server>
```

## Monitoring and Maintenance

### Logging
```python
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Health Check Endpoint
```python
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200
```

## Performance Optimization

1. **Enable caching** (Redis)
2. **Compress responses** (Flask-Compress)
3. **Optimize images** (WebP format)
4. **Use CDN** for static files
5. **Enable database connection pooling**
6. **Implement lazy loading**
7. **Minify CSS/JS**

## Security Hardening

1. Enable HTTPS
2. Add security headers
3. Implement rate limiting
4. Enable CORS properly
5. Add input validation
6. Sanitize file uploads
7. Use secrets manager

## Backup Strategy

```bash
# Automated daily backups
0 2 * * * pg_dump database > backup-$(date +\%Y\%m\%d).sql
```

## Cost Optimization

- Use free tiers initially (Heroku, Railway)
- Enable auto-scaling based on traffic
- Optimize model inference (quantization)
- Use spot instances for non-critical workloads
- Implement caching to reduce API calls

For more help, consult platform-specific documentation!
