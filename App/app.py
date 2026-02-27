import os
from flask import Flask, redirect, render_template, request, jsonify, session, flash, url_for, make_response, Response, stream_with_context
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import psutil
from typing import IO
from io import BytesIO
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///plantsecure.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Session(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


#Checking cache and ensuring that the browser does not cache the page when the user logout 
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


# User Class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    profile_image = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f'User("{self.id}", "{self.fullname}", "{self.username}", "{self.email}", "{self.profile_image}")'
    

# Disease Prediction Class
class DiseasePrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    disease_name = db.Column(db.String(150), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'DiseasePrediction("{self.id}", "{self.user_id}", "{self.disease_name}", "{self.timestamp}")'

# Admin Class
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    profile_image = db.Column(db.String(150), nullable=True)  # Add this line

    def __repr__(self):
        return f'Admin("{self.id}", "{self.fullname}", "{self.username}", "{self.email}", "{self.profile_image}")'

def insert_admin():
    if not Admin.query.filter_by(username="albertstone").first() and not Admin.query.filter_by(email="plantsecureadmin@gmail.com").first():
        hashed_password = bcrypt.generate_password_hash('plantsecureAdmin').decode('utf-8')
        admin = Admin(
            fullname="Albert Amoako",
            username="albertstone",
            email="plantsecureadmin@gmail.com",
            password=hashed_password
        )
        db.session.add(admin)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) or Admin.query.get(int(user_id))

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

# Initialize the database and create tables
with app.app_context():
    db.create_all()
    insert_admin()



# Load environment variables
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Initialize Eleven client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def generate_audio_stream(text: str):
    response = client.text_to_speech.convert(
        voice_id="TX3LPaxmHKxFdv7VOQHJ", # LIAM voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    for chunk in response:
        if chunk:
            yield chunk

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({"error": "Text is required"}), 400

    return Response(stream_with_context(generate_audio_stream(text)), mimetype='audio/mpeg')


# INDEX PAGE ROUTE 
@app.route('/')
def main_home_page():
    return render_template('/homepage_main/main-index.html')

#DETECT DISEASE PAGE ROUTE
@app.route('/plantsecure_detect_disease')
@login_required
def ai_engine_page():
    return render_template('index.html')

#MOBILE DEVICE DETECTED PAGE
@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')


#WEATHER APP ROUTE
@app.route('/plantsecure_realtime_weather_tracking')
@login_required
def weatherapp():
    return render_template('/weatherapp/index.html')

#ML ENGINE HOME PAGE ROUTE
@app.route('/mlengine_home')
@login_required
def user_home_page():
    return render_template('home.html')

#USER LOGIN ROUTE
@app.route('/login')
def login():
    return render_template('/homepage_main/auth-signin.html')

#ADMIN LOGIN ROUTE
@app.route('/admin_login')
def admin_login():
    return render_template('/homepage_main/admin-login.html')


#USER SIGNIN LOGIC & ROUTE
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect(url_for('user_home_page'))
    else:
        flash('Login unsuccessful. Please check username and password', 'danger')
        return redirect(url_for('login'))
    


#ADMIN SIGNIN LOGIC & ROUTE
@app.route('/admin_login', methods=['POST'])
def admin_login_post():
    username = request.form['username']
    password = request.form['password']
    
    admin = Admin.query.filter_by(username=username).first()

    if admin and bcrypt.check_password_hash(admin.password, password):
        login_user(admin)
        session['user_id'] = admin.id
        session['username'] = admin.username
        session['user_type'] = 'Admin'  # Set the user type to Admin
        flash('Admin login successful!', 'success')
        return redirect(url_for('admin_dashboard'))
    else:
        flash('Login unsuccessful. Please check username and password', 'danger')
        return redirect(url_for('admin_login'))


#USER SIGNUP LOGIC
@app.route('/signup', methods=['POST'])
def signup_post():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return redirect(url_for('signup'))

    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists', 'danger')
        return redirect(url_for('signup'))

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exists', 'danger')
        return redirect(url_for('signup'))

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(fullname=fullname, username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    flash('Signup successful! Please log in.', 'success')
    return redirect(url_for('login'))


#UPDATE USER PROFILE LOGIC -- USER END
@app.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    fullname = request.form.get('fullname') or current_user.fullname
    username = request.form.get('username') or current_user.username
    email = request.form.get('email') or current_user.email
    profile_image = request.files.get('profile_image')

    if profile_image:
        profile_image_filename = f"{current_user.id}_{profile_image.filename}"
        profile_image.save(os.path.join('static/user_dash_assets/img/profiles', profile_image_filename))
        current_user.profile_image = profile_image_filename

    current_user.fullname = fullname
    current_user.username = username
    current_user.email = email

    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('user_profile_dashboard'))


#CHANGE USER PASSWORD --- USER END
@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']

        if not bcrypt.check_password_hash(current_user.password, current_password):
            flash('Password update unsuccessful. Current password is incorrect', 'danger')
            return redirect(url_for('change_password'))

        if new_password != confirm_new_password:
            flash('New passwords do not match', 'danger')
            return redirect(url_for('change_password'))

        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        current_user.password = hashed_password
        db.session.commit()

        flash('Password updated successfully!', 'success')
        return redirect(url_for('user_profile_dashboard'))

    return render_template('user_dashboard/profile.html')


#Delete user account logic. User deleting his own account
@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    user = current_user
    db.session.delete(user)
    db.session.commit()
    logout_user()
    session.pop('user_id', None)
    session.pop('user_type', None)
    session.pop('username', None)
    flash('Your account has been deleted successfully.', 'success')
    return redirect(url_for('login'))


#ADMIN ADD USER -- LOGIC
@app.route('/admin/add_user', methods=['POST'])
@login_required
def add_user():
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('admin_dashboard'))

    fullname = request.form.get('fullname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return redirect(url_for('admin_dashboard'))

    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists', 'danger')
        return redirect(url_for('admin_dashboard'))

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exists', 'danger')
        return redirect(url_for('admin_dashboard'))

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(fullname=fullname, username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    flash('User added successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

#ADMIN EDIT SPECIFIED USER LOGIC
@app.route('/admin/edit_user/<int:user_id>', methods=['POST'])
@login_required
def edit_user(user_id):
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('admin_dashboard'))

    user = User.query.get_or_404(user_id)
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    email = request.form.get('email')
    new_password = request.form.get('new_password')
    confirm_new_password = request.form.get('confirm_new_password')

    if new_password and new_password != confirm_new_password:
        flash('New passwords do not match for the specified user. Please try again.', 'danger')
        return redirect(url_for('admin_dashboard'))

    user.fullname = fullname
    user.username = username
    user.email = email

    if new_password:
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        user.password = hashed_password

    db.session.commit()
    flash('User details updated successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

#ADMIN DELETE USER LOGIC
@app.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('admin_dashboard'))

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/user-dashboard')
@login_required
def user_profile_dashboard():
    return render_template('user_dashboard/profile.html')

#LOGOUT USER LOGIC
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('user_id', None)
    session.pop('user_type', None)
    session.pop('username', None)
    session.pop('_flashes', None)  # Remove any flash messages
    response = redirect(url_for('login'))
    response.set_cookie('session', '', expires=0)  # Expire the session cookie immediately
    response.set_cookie('logged_in', '', expires=0)  # Expire the logged_in cookie immediately
    return response


#SIGNUP ROUTE FOR USER
@app.route('/signup')
def signup():
    return render_template('/homepage_main/auth-signup.html')

#FORGOT PASSWORD ROUTE FOR USER
@app.route('/forgot-password')
def forgot_password():
    return render_template('homepage_main/auth-forgot-password.html')

#HANDLING INFORMATION ON THE ADMIN DASHBOARD
@app.route('/admin-dashboard')
@login_required
def admin_dashboard():
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main_home_page'))

    total_admins = Admin.query.count()
    total_regular_users = User.query.count()
    users = User.query.all()  # Fetch all users

    # Fetch the current admin's username from the Admin table
    admin = Admin.query.get(session['user_id'])
    admin_username = admin.username if admin else 'Unknown'

    # Gather system performance data
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    # Fetch disease prediction data
    total_predictions = DiseasePrediction.query.count()
    recent_predictions = DiseasePrediction.query.order_by(DiseasePrediction.timestamp.desc()).limit(5).all()
    common_diseases = db.session.query(DiseasePrediction.disease_name, db.func.count(DiseasePrediction.disease_name).label('count')).group_by(DiseasePrediction.disease_name).order_by(db.desc('count')).limit(5).all()

    return render_template(
        'admin_dashboard/admin-dashboard.html',
        total_admins=total_admins,
        total_regular_users=total_regular_users,
        users=users,
        admin_username=admin_username,
        admin=admin,  # Pass the admin object to the template
        cpu_usage=cpu_usage,
        memory_info=memory_info,
        disk_usage=disk_usage,
        total_predictions=total_predictions,
        recent_predictions=recent_predictions,
        common_diseases=common_diseases
    )

@app.route('/clear_history', methods=['POST'])
@login_required
def clear_history():
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('admin_dashboard'))

    # Clear the DiseasePrediction table
    db.session.query(DiseasePrediction).delete()
    db.session.commit()

    flash('History cleared successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


#Admin profile logic
@app.route('/admin-profile')
@login_required
def admin_profile():
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main_home_page'))

    admin = Admin.query.get(session['user_id'])
    return render_template('admin_dashboard/profile.html', admin=admin)

#UPDATE ADMIN PROFILE
@app.route('/admin/update_profile', methods=['POST'])
@login_required
def admin_update_profile():
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('admin_dashboard'))

    admin = Admin.query.get(session['user_id'])
    fullname = request.form.get('fullname') or admin.fullname
    username = request.form.get('username') or admin.username
    email = request.form.get('email') or admin.email
    profile_image = request.files.get('profile_image')

    if profile_image:
        profile_image_filename = f"{admin.id}_{profile_image.filename}"
        profile_image.save(os.path.join('static/admin_assets/img/profiles', profile_image_filename))
        admin.profile_image = profile_image_filename  # Save the filename to the database

    admin.fullname = fullname
    admin.username = username
    admin.email = email

    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('admin_profile'))


# Change Admin Password Logic
@app.route('/admin/change_password', methods=['GET', 'POST'])
@login_required
def admin_change_password():
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('main_home_page'))

    admin = Admin.query.get(session['user_id'])

    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']

        if not bcrypt.check_password_hash(admin.password, current_password):
            flash('Password update unsuccessful. Current password is incorrect', 'danger')
            return redirect(url_for('admin_change_password'))

        if new_password != confirm_new_password:
            flash('New passwords do not match', 'danger')
            return redirect(url_for('admin_change_password'))

        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        admin.password = hashed_password
        db.session.commit()

        flash('Password updated successfully!', 'success')
        return redirect(url_for('admin_profile'))

    return render_template('admin_dashboard/profile.html', admin=admin)


#Delete Admin Account Logic
@app.route('/delete_admin_account', methods=['POST'])
@login_required
def delete_admin_account():
    if session.get('user_type') != 'Admin':
        flash('You do not have permission to perform this action.', 'danger')
        return redirect(url_for('main_home_page'))

    admin = Admin.query.get(current_user.id)
    if admin:
        db.session.delete(admin)
        db.session.commit()
        logout_user()
        session.pop('user_id', None)
        session.pop('user_type', None)
        session.pop('username', None)
        flash('Your account has been deleted successfully.', 'success')
        return redirect(url_for('login'))
    else:
        flash('Admin account not found.', 'danger')
        return redirect(url_for('admin_profile'))



#DISEASE PREDICTION CODE LOGIC 
disease_info = pd.read_csv('disease_info.csv', encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv', encoding='cp1252')

model = CNN.CNN(39)
model.load_state_dict(torch.load("plant_disease_model_1_latest.pt"))
model.eval()

def prediction(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index

#PLANT DISEASE IMAGE SUBMIT LOGIC & ROUTE
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('static/uploads', filename)
        image.save(file_path)
        # print(file_path)  # Debug: Uncomment for troubleshooting
        pred = prediction(file_path)
        title = disease_info['disease_name'][pred]
        description = disease_info['description'][pred]
        prevent = disease_info['Possible Steps'][pred]
        image_url = disease_info['image_url'][pred]
        supplement_name = supplement_info['supplement name'][pred]
        supplement_image_url = supplement_info['supplement image'][pred]
        supplement_buy_link = supplement_info['buy link'][pred]

        # Save the prediction to the database
        if current_user.is_authenticated:
            disease_prediction = DiseasePrediction(user_id=current_user.id, disease_name=title)
            db.session.add(disease_prediction)
            db.session.commit()

        return render_template('submit.html', title=title, desc=description, prevent=prevent,
        image_url=image_url, pred=pred, sname=supplement_name, simage=supplement_image_url, buy_link=supplement_buy_link)


#Marketplace Code
@app.route('/plantsecure_marketplace', methods=['GET', 'POST'])
@login_required
def market():
    return render_template('market.html', supplement_image=list(supplement_info['supplement image']),
    supplement_name=list(supplement_info['supplement name']), disease=list(disease_info['disease_name']), buy=list(supplement_info['buy link']))

if __name__ == '__main__':
    app.run(debug=True)