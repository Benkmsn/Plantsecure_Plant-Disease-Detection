# 🌿 PlantSecure - AI-Powered Plant Disease Detection System

<div align="center">

![PlantSecure](https://img.shields.io/badge/Version-1.0.0-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)
![PyTorch](https://img.shields.io/badge/PyTorch-1.8+-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

**An intelligent web application that uses Deep Learning to detect plant diseases from leaf images and provides actionable treatment recommendations.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Technologies](#-technologies-used) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents
- [About](#-about-the-project)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Model Information](#-model-information)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)

---

## 🌟 About The Project

**PlantSecure** is a comprehensive plant disease detection and management system developed as a final year academic project. The application leverages **Convolutional Neural Networks (CNN)** to identify 39 different plant diseases and healthy conditions across 14 plant species with high accuracy.

### Problem Statement
Plant diseases cause significant crop losses worldwide, and early detection is crucial for effective treatment. However, many farmers lack access to expert plant pathologists, leading to delayed diagnosis and reduced yields.

### Solution
PlantSecure provides an accessible, AI-powered solution that enables instant disease detection through simple leaf image uploads, offering:
- Real-time disease diagnosis
- Detailed treatment recommendations
- Marketplace for disease-specific supplements
- Weather tracking for informed farming decisions

---

## ✨ Features

### 🔬 Core Functionality
- **AI-Powered Disease Detection**: Upload plant leaf images and get instant diagnosis using a custom-trained CNN model
- **39 Disease Classifications**: Identifies diseases across 14 plant species including Apple, Tomato, Corn, Grape, Potato, and more
- **Comprehensive Disease Information**: 
  - Detailed disease descriptions
  - Prevention and treatment steps
  - Reference images
  - Supplement recommendations with purchase links

### 👥 User Management
- **Multi-Role Authentication System**: Separate login flows for regular users and administrators
- **User Profiles**: Profile management with image upload, password change, and account settings
- **Secure Authentication**: BCrypt password hashing and session management

### 🎯 Admin Dashboard
- **User Management**: Add, edit, and delete user accounts
- **System Monitoring**: Real-time CPU, memory, and disk usage tracking
- **Analytics Dashboard**:
  - Total prediction statistics
  - Recent disease predictions
  - Most common diseases detected
  - Historical data management

### 🌤️ Weather Integration
- **Real-Time Weather Data**: Current weather conditions for any location
- **5-Day Forecast**: Extended weather predictions
- **Location Services**: Search by city or use current GPS location
- **Agricultural Insights**: Temperature, humidity, and air quality data

### 🛒 Marketplace
- **Product Recommendations**: Disease-specific fertilizers and supplements
- **Categorized Browsing**: Filter between fertilizers and supplements
- **Direct Purchase Links**: Quick access to product vendors

### 🔊 Accessibility
- **Text-to-Speech**: AI voice narration of disease information using ElevenLabs API
- **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices

---

## 🛠 Technologies Used

### Backend
- **Framework**: Flask (Python)
- **Machine Learning**: PyTorch
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Session Management**: Flask-Session
- **Image Processing**: Pillow (PIL)
- **Data Processing**: Pandas, NumPy

### Frontend
- **HTML5, CSS3, JavaScript**
- **Bootstrap 5**: Responsive UI framework
- **Font Awesome & Ionicons**: Icon libraries
- **Custom CSS**: Tailored styling for enhanced UX

### APIs & Services
- **ElevenLabs API**: Text-to-speech functionality
- **OpenWeatherMap API**: Weather data and forecasts
- **Geocoding API**: Location services

### Development Tools
- **Version Control**: Git & GitHub
- **Environment Management**: Python virtual environments
- **Package Management**: pip

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│          (HTML/CSS/JavaScript + Bootstrap)                   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    Flask Application                         │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Auth       │  │   Disease    │  │   Weather    │     │
│  │   Module     │  │   Detection  │  │   Module     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Admin      │  │  Marketplace │  │   TTS        │     │
│  │   Dashboard  │  │   Module     │  │   Module     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   CNN Model  │ │   SQLite DB  │ │ External APIs│
│   (PyTorch)  │ │  (SQLAlchemy)│ │  (Weather,   │
│              │ │              │ │   TTS)       │
└──────────────┘ └──────────────┘ └──────────────┘
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Benkmsn/Plantsecure_Plant-Disease-Detection.git
   cd Plantsecure_Plant-Disease-Detection
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd App
   pip install -r requirements.txt
   ```

4. **Download the trained model**
   
   The model file is large and not included in the repository. Download it from:
   - [Google Drive Link]( https://drive.google.com/file/d/1IDCMmc2OF570yBZGd3Dpw_3uN4danTxH/view?usp=sharing)
   - Save `plant_disease_model_1_latest.pt` in the `App/` directory

5. **Set up environment variables**
   ```bash
   # Create .env file in App/ directory
   cp .env.example .env
   
   # Edit .env with your API keys
   ```

6. **Initialize the database**
   ```bash
   python app.py
   # Database will be created automatically on first run
   ```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the `App/` directory with the following:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# API Keys
ELEVENLABS_API_KEY=your-elevenlabs-api-key
OPENWEATHER_API_KEY=your-openweather-api-key

# Database
SQLALCHEMY_DATABASE_URI=sqlite:///plantsecure.sqlite
```

### API Keys Setup

1. **ElevenLabs API** (Text-to-Speech):
   - Sign up at [ElevenLabs](https://elevenlabs.io/)
   - Get your API key from the dashboard
   - Add to `.env` file

2. **OpenWeatherMap API** (Weather Data):
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Get free API key
   - Update in `static/weatherapp_assets/script.js` (line 4) or add to `.env`

### Default Admin Credentials
- **Username**: `albertstone`
- **Email**: `plantsecureadmin@gmail.com`
- **Password**: `plantsecureAdmin`

**⚠️ Important**: Change the default admin password after first login!

---

## 🚀 Usage

### Starting the Application

```bash
cd App
python app.py
```

The application will be available at: `http://localhost:5000`

### User Workflow

1. **Registration/Login**
   - Navigate to the homepage
   - Sign up for a new account or log in

2. **Disease Detection**
   - Go to "Detect Disease" page
   - Upload a clear image of a plant leaf
   - Click "Submit" to analyze
   - View detailed results with treatment recommendations

3. **Explore Features**
   - Check real-time weather for your location
   - Browse marketplace for recommended products
   - Update your profile settings

### Admin Workflow

1. **Admin Login**
   - Navigate to `/admin_login`
   - Use admin credentials
   
2. **Dashboard Management**
   - Monitor system performance
   - View prediction analytics
   - Manage user accounts
   - Clear prediction history

---

## 🧠 Model Information

### Architecture: Custom CNN

**Model Specifications:**
- **Input Size**: 224 × 224 × 3 (RGB images)
- **Architecture**:
  ```
  Conv2D(3→32) → BatchNorm → ReLU → Conv2D(32→32) → BatchNorm → ReLU → MaxPool2D
  Conv2D(32→64) → BatchNorm → ReLU → Conv2D(64→64) → BatchNorm → ReLU → MaxPool2D
  Conv2D(64→128) → BatchNorm → ReLU → Conv2D(128→128) → BatchNorm → ReLU → MaxPool2D
  Conv2D(128→256) → BatchNorm → ReLU → Conv2D(256→256) → BatchNorm → ReLU → MaxPool2D
  Flatten → Dropout(0.4) → Dense(50176→1024) → ReLU → Dropout(0.4) → Dense(1024→39)
  ```
- **Output Classes**: 39 (38 diseases + 1 healthy/background class)
- **Framework**: PyTorch
- **Training Dataset**: PlantVillage Dataset (~61,486 images)

### Supported Plant Species
- 🍎 Apple
- 🫐 Blueberry
- 🍒 Cherry
- 🌽 Corn (Maize)
- 🍇 Grape
- 🍊 Orange
- 🍑 Peach
- 🫑 Bell Pepper
- 🥔 Potato
- 🍓 Raspberry
- 🫘 Soybean
- 🥒 Squash
- 🍓 Strawberry
- 🍅 Tomato

### Detected Diseases (Sample)
- Apple: Scab, Black Rot, Cedar Apple Rust
- Tomato: Early Blight, Late Blight, Leaf Mold, Bacterial Spot, Septoria Leaf Spot
- Corn: Common Rust, Northern Leaf Blight, Gray Leaf Spot
- Grape: Black Rot, Esca, Leaf Blight
- Potato: Early Blight, Late Blight
- And 20+ more diseases...

---

## 📁 Project Structure

```
PlantSecure/
│
├── App/
│   ├── app.py                      # Main Flask application
│   ├── CNN.py                      # CNN model architecture
│   ├── requirements.txt            # Python dependencies
│   ├── disease_info.csv            # Disease database
│   ├── supplement_info.csv         # Product recommendations
│   ├── plant_disease_model_1_latest.pt  # Trained model (download separately)
│   │
│   ├── templates/                  # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── submit.html
│   │   ├── market.html
│   │   ├── homepage_main/
│   │   ├── admin_dashboard/
│   │   ├── user_dashboard/
│   │   └── weatherapp/
│   │
│   ├── static/                     # Static assets
│   │   ├── main_assets/
│   │   ├── admin_assets/
│   │   ├── user_dash_assets/
│   │   ├── weatherapp_assets/
│   │   └── uploads/                # User uploaded images
│   │
│   ├── instance/
│   │   └── plantsecure.sqlite      # Database file
│   │
│   └── flask_session/              # Session storage
│
├── Model/
│   ├── Plant Disease Detection Code.ipynb   # Training notebook
│   └── Readme.md                             # Model documentation
│
├── .gitignore
├── LICENSE
└── README.md                       # This file
```

---

## 🌐 API Endpoints

### Authentication
- `GET /` - Landing page
- `GET/POST /login` - User login
- `GET/POST /signup` - User registration
- `GET/POST /admin_login` - Admin login
- `GET /logout` - Logout

### Disease Detection
- `GET /plantsecure_detect_disease` - Detection page
- `POST /submit` - Submit image for analysis
- `POST /text_to_speech` - Convert text to speech

### User Management
- `GET /user-dashboard` - User profile
- `POST /update_profile` - Update user profile
- `POST /change_password` - Change password
- `POST /delete_account` - Delete account

### Admin
- `GET /admin-dashboard` - Admin panel
- `POST /admin/add_user` - Add new user
- `POST /admin/edit_user/<id>` - Edit user
- `POST /admin/delete_user/<id>` - Delete user
- `POST /clear_history` - Clear prediction history

### Features
- `GET /plantsecure_marketplace` - Product marketplace
- `GET /plantsecure_realtime_weather_tracking` - Weather app

---


---

## 🔮 Possible Future Enhancements

- [ ] **Mobile Application**: Develop native iOS and Android apps
- [ ] **Improved Model**: Train on larger datasets for higher accuracy
- [ ] **Real-Time Detection**: Implement video stream analysis
- [ ] **Multi-Language Support**: Internationalization for global users
- [ ] **Community Forum**: Allow farmers to share experiences
- [ ] **Expert Consultation**: Connect users with agricultural experts
- [ ] **Crop Health Monitoring**: Track plant health over time
- [ ] **Pest Detection**: Expand to identify common plant pests
- [ ] **Drone Integration**: Analyze aerial crop imagery

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
---

## 🙏 Acknowledgments

- **Dataset**: [PlantVillage Dataset](https://data.mendeley.com/datasets/tywbtsjrjv/1)
- **Inspiration**: The need for accessible agricultural disease diagnosis
- **APIs**: ElevenLabs, OpenWeatherMap
- **Community**: PyTorch and Flask communities

---

