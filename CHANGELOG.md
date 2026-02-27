# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-27

### Added
- Initial release of PlantSecure
- AI-powered plant disease detection using CNN
- 39 disease classifications across 14 plant species
- User authentication and authorization system
- Admin dashboard with analytics
- Real-time weather tracking integration
- Plant supplement marketplace
- Text-to-speech functionality for accessibility
- Responsive web design for mobile and desktop
- User profile management
- Disease prediction history tracking
- System performance monitoring in admin panel

### Features
- Custom CNN model with 4 convolutional layers
- Flask-based web application
- SQLite database with SQLAlchemy ORM
- BCrypt password hashing for security
- Session-based authentication
- File upload for image analysis
- CSV-based disease and supplement information
- OpenWeatherMap API integration
- ElevenLabs TTS API integration

### Security
- Password hashing with BCrypt
- Session management with Flask-Session
- Environment variable configuration
- CSRF protection
- Input validation

### Documentation
- Comprehensive README with installation guide
- Code comments and docstrings
- Contributing guidelines
- Security policy
- Setup guide
- Deployment guide

---

## [Unreleased]

### Planned Features
- [ ] Mobile application (iOS/Android)
- [ ] Real-time video stream analysis
- [ ] Multi-language support
- [ ] Offline mode
- [ ] Community forum
- [ ] Expert consultation booking
- [ ] Crop health tracking over time
- [ ] Pest detection
- [ ] Drone integration
- [ ] REST API for third-party integrations

### Known Issues
- Weather API key exposed in client-side JavaScript (needs backend proxy)
- Large model file not versioned (requires external download)
- Limited to SQLite database (recommend PostgreSQL for production)

---

## Version History

- **1.0.0** (2026-02-27) - Initial Release

---

For detailed changes, see the [commit history](https://github.com/Benkmsn/Plantsecure_Plant-Disease-Detection/commits/main).
