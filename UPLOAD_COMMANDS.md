# Quick Pre-Upload Commands

**Copy and paste these commands before pushing to GitHub:**

```bash
# Navigate to project root
cd "c:\Users\KB\Documents\PlantSecure"

# 1. CRITICAL: Remove virtual environment folder (it's huge!)
# Option A: If not tracked by git yet
rmdir /s /q App\venvScriptsactivate

# Option B: If already tracked by git
git rm -r --cached App/venvScriptsactivate
rmdir /s /q App\venvScriptsactivate

# 2. Check what will be committed (IMPORTANT!)
git status

# 3. Verify these are NOT showing up:
#    ❌ .env
#    ❌ venvScriptsactivate/
#    ❌ instance/plantsecure.sqlite
#    ❌ flask_session/
#    ❌ __pycache__/
#    ❌ *.pt (model files)

# 4. If any sensitive files appear, remove them:
git rm --cached App/.env
git rm --cached App/instance/plantsecure.sqlite
git rm -r --cached App/flask_session

# 5. Stage all files
git add .

# 6. Check again what will be committed
git status

# 7. Commit
git commit -m "Initial commit: PlantSecure AI Plant Disease Detection System

- Custom CNN model for 39 plant disease classifications
- Flask web application with user authentication
- Admin dashboard with analytics
- Real-time weather integration
- Marketplace for supplements
- Comprehensive documentation and deployment guides"

# 8. Add remote (if not already added)
git remote add origin https://github.com/Benkmsn/Plantsecure_Plant-Disease-Detection.git

# 9. Push to GitHub
git push -u origin main

# If main doesn't exist, use master:
# git push -u origin master

# 10. If push is rejected, try:
git pull origin main --rebase
git push -u origin main
```

## After Successful Upload:

```bash
# Go to GitHub repository settings and:
# 1. Add description
# 2. Add topics/tags
# 3. Update About section

# Then take screenshots and update README with images:
# - Edit README.md
# - Replace screenshot paths
# - Commit and push again
```

## Verify Upload Success:

Visit your repository and check:
- [ ] README displays correctly
- [ ] No .env file visible
- [ ] No database files visible
- [ ] No venv folder visible
- [ ] Model files (.pt) not visible
- [ ] License shows up
- [ ] Topics/tags are added
- [ ] Installation instructions are clear
