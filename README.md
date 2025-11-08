# Patient Emergency Priority System - Backend

A Flask-based REST API backend for managing patient emergencies and priorities in a healthcare setting.

## Features

- **RESTful API Endpoints**
  - GET /patients - Retrieve all patients sorted by priority
  - POST /patients - Add a new patient
  - DELETE /patients/{id} - Remove a patient

- **Priority-Based System**
  - Priority levels 1-5
  - Automatic sorting by priority
  - Built-in validation

- **Database Integration**
  - SQLite database with SQLAlchemy ORM
  - Automatic schema management
  - Transaction support

## Tech Stack

- Python 3.9
- Flask 2.0.1
- Flask-SQLAlchemy 2.5.1
- Flask-CORS 3.0.10
- Gunicorn 20.1.0
- SQLite Database

## Project Structure

```
backend/
│
├── app/                    # Application package
│   ├── __init__.py        # App initialization and factory
│   ├── models.py          # Database models
│   ├── routes.py          # API endpoints
│   ├── utils.py           # Utility functions
│   └── config.py          # Configuration settings
│
├── requirements.txt        # Python dependencies
├── run.py                 # Application entry point
├── Dockerfile             # Docker configuration
├── gunicorn.conf.py       # Gunicorn server config
└── .dockerignore          # Docker build exclusions
```

## API Endpoints

### Get All Patients
```http
GET /patients
```
Response:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 45,
    "condition": "Cardiac Issue",
    "priority": 4,
    "arrival_time": "2025-11-08T10:30:00"
  }
]
```

### Add New Patient
```http
POST /patients
Content-Type: application/json

{
  "name": "Jane Smith",
  "age": 28,
  "condition": "Broken Arm",
  "priority": 3
}
```

### Delete Patient
```http
DELETE /patients/{patient_id}
```

## Setup and Installation

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Development Server**
   ```bash
   python run.py
   ```

4. **Run with Gunicorn (Production)**
   ```bash
   gunicorn --conf gunicorn.conf.py --bind 0.0.0.0:5000 run:app
   ```

## Docker Deployment

1. **Build Image**
   ```bash
   docker build -t patient-system-backend .
   ```

2. **Run Container**
   ```bash
   docker run -p 5000:5000 patient-system-backend
   ```

## Environment Variables

- `FLASK_APP`: Set to run.py
- `FLASK_ENV`: 'development' or 'production'
- `DATABASE_URL`: SQLite database URL (default: sqlite:///patients.db)
- `SECRET_KEY`: Application secret key

## Database Schema

### Patient Model
```python
class Patient:
    id: Integer (Primary Key)
    name: String(100)
    age: Integer
    condition: String(200)
    priority: Integer
    arrival_time: DateTime
```

## Error Handling

The API includes comprehensive error handling for:
- Invalid input data
- Missing required fields
- Database errors
- Resource not found (404)
- Server errors (500)

## Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Document functions and classes

### Testing
```bash
# Run tests (if implemented)
python -m pytest
```

### Adding New Features
1. Create new routes in routes.py
2. Update models if needed
3. Add necessary validation
4. Test thoroughly
5. Update documentation

## Security Features

- CORS support for frontend integration
- Input validation
- Error handling
- Database transaction management
- Production-ready with Gunicorn

## Performance Considerations

- Database indexing on priority field
- Efficient query optimization
- Connection pooling
- Response caching (if implemented)

## Monitoring

- Gunicorn worker management
- Application logging
- Error tracking
- Performance metrics

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is part of the Patient Emergency Priority System.
Copyright © 2025. All rights reserved.