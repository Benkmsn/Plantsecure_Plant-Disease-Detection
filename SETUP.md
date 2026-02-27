# Quick Setup Guide

## Prerequisites Checklist
- [ ] Python 3.8+ installed
- [ ] Git installed
- [ ] Virtual environment tool (venv)
- [ ] Internet connection for API services

## Installation Steps

### 1. Clone and Navigate
```bash
git clone https://github.com/Benkmsn/Plantsecure_Plant-Disease-Detection.git
cd Plantsecure_Plant-Disease-Detection/App
```

### 2. Create Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Download Model File
1. Visit: https://drive.google.com/drive/folders/1ewJWAiduGuld_9oGSrTuLumg9y62qS6A?usp=share_link
2. Download `plant_disease_model_1_latest.pt`
3. Place it in the `App/` directory

### 5. Configure Environment Variables
```bash
# Copy example file
cp .env.example .env

# Edit .env with your API keys
# Windows: notepad .env
# Linux/Mac: nano .env
```

Required API Keys:
- **SECRET_KEY**: Generate using `python -c "import secrets; print(secrets.token_hex(32))"`
- **ELEVENLABS_API_KEY**: Get from https://elevenlabs.io/
- **OPENWEATHER_API_KEY**: Get from https://openweathermap.org/api

### 6. Update Weather API Key in JavaScript
Edit `static/weatherapp_assets/script.js` line 4:
```javascript
api_key = 'YOUR_OPENWEATHER_API_KEY_HERE'
```

### 7. Run the Application
```bash
python app.py
```

Visit: http://localhost:5000

## Default Login Credentials

**Admin Account:**
- Username: `albertstone`
- Email: `plantsecureadmin@gmail.com`
- Password: `plantsecureAdmin`

**⚠️ IMPORTANT**: Change admin password after first login!

## Troubleshooting

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Module Not Found Error
```bash
pip install --upgrade -r requirements.txt
```

### Database Error
```bash
# Delete and recreate database
rm instance/plantsecure.sqlite
python app.py
```

### Model File Error
Ensure `plant_disease_model_1_latest.pt` is in the `App/` directory, not in subdirectories.

## Next Steps
1. Create a regular user account
2. Test disease detection with sample leaf images
3. Explore admin dashboard features
4. Check weather integration
5. Browse marketplace

## Need Help?
- Check the main [README.md](../README.md)
- Open an issue on GitHub
- Contact the maintainer

Good luck! 🌿
