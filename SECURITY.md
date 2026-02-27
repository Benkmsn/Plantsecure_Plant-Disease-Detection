# Security Policy

## Supported Versions

Currently supported versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in PlantSecure, please follow these steps:

1. **DO NOT** open a public issue
2. Email the maintainer at: [your.email@example.com]
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work on a fix promptly.

## Security Best Practices for Users

### Before Deploying to Production:

1. **Change Default Credentials**
   - Update default admin password immediately
   - Use strong, unique passwords

2. **Secure Environment Variables**
   - Never commit `.env` file to version control
   - Use secure methods to store API keys in production
   - Rotate API keys regularly

3. **Database Security**
   - Use PostgreSQL or MySQL instead of SQLite in production
   - Enable database encryption
   - Regular backups

4. **Application Security**
   - Set `FLASK_DEBUG=False` in production
   - Use HTTPS (SSL/TLS certificates)
   - Implement rate limiting
   - Add CORS policies
   - Enable CSRF protection

5. **File Upload Security**
   - Validate file types and sizes
   - Scan uploads for malware
   - Store uploads outside web root

6. **Session Security**
   - Use secure session configuration
   - Set appropriate session timeouts
   - Enable secure cookies

### Example Production Configuration:

```python
# app.py - Production settings
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=timedelta(hours=1)
)
```

## Known Security Considerations

1. **API Keys**: Current implementation has OpenWeatherMap API key in client-side JavaScript. For production, proxy these requests through your backend.

2. **File Uploads**: Implement additional validation and virus scanning before processing uploaded images.

3. **Rate Limiting**: Add rate limiting to prevent abuse of the disease detection endpoint.

## Security Updates

Security updates will be released as patch versions. Subscribe to repository notifications to stay informed.
