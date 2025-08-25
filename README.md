# Student Registration Form

A modern, responsive student registration application built with FastAPI (backend) and React (frontend).

## Features

- ✨ Beautiful, modern UI with glassmorphism effects
- 📱 Fully responsive design
- 🔒 Form validation with detailed error messages
- 🎨 Gradient background with subtle patterns
- ⚡ Fast API with SQLite database
- 🔄 Real-time form submission with loading states
- 📊 Student data management

## Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **Poetry** - Dependency management

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **CSS3** - Modern styling with animations

## Project Structure

```
STUDENT-FORM/
├── backend_fastapi/
│   ├── 01_sqlite.py          # Main FastAPI application
│   ├── database.py           # Database configuration
│   ├── models.py             # SQLAlchemy models
│   ├── pydantic_models.py    # Pydantic schemas
│   ├── student_form.db       # SQLite database
│   └── pyproject.toml        # Poetry configuration
└── frontend_react/
    └── student_form_app/
        ├── src/
        │   ├── App.js         # Main React component
        │   └── App.css        # Styling
        └── package.json       # Node.js dependencies
```

## Setup Instructions

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend_fastapi
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

3. **Run the FastAPI server:**
   ```bash
   poetry run uvicorn 01_sqlite:app --reload
   ```

   The backend will be available at: `http://localhost:8000`

4. **API Documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend_react/student_form_app
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

   The frontend will be available at: `http://localhost:3000`

## API Endpoints

### POST `/students/`
Create a new student registration.

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "cnic": "33100-2234567-1",
  "date_of_birth": "1995-05-15",
  "phone_number": "03001234567",
  "address": "123 Main Street, City",
  "degree": "BSc Computer Science"
}
```

### GET `/students/`
Retrieve all registered students.

### GET `/students/{student_id}`
Retrieve a specific student by ID.

## Form Validation Rules

- **First Name & Last Name**: 1-50 characters, required
- **Email**: Valid email format, unique, required
- **CNIC**: Format XXXXX-XXXXXXX-X, unique, required
- **Date of Birth**: Must be between 15-100 years old
- **Phone Number**: Format 03XXXXXXXXX (optional)
- **Address**: Maximum 200 characters (optional)
- **Degree**: 1-100 characters, required

## Features

### Backend Features
- ✅ RESTful API with FastAPI
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Pydantic data validation
- ✅ CORS middleware for frontend integration
- ✅ Comprehensive error handling
- ✅ Duplicate email/CNIC prevention
- ✅ API documentation with Swagger

### Frontend Features
- ✅ Modern, responsive design
- ✅ Glassmorphism UI effects
- ✅ Real-time form validation
- ✅ Loading states and animations
- ✅ Error and success message handling
- ✅ Mobile-friendly layout
- ✅ Beautiful gradient background

## Screenshots

<img width="960" height="539" alt="Screenshot_5" src="https://github.com/user-attachments/assets/42701e90-a024-4b04-bda2-44769c268bdc" /><img width="507" height="510" alt="Screenshot_4" src="https://github.com/user-attachments/assets/ad7248e6-f444-42fd-b191-ebe68d88815b" />

The application features:
- A beautiful gradient background with subtle grid patterns
- Glassmorphism form container with blur effects
- Responsive design that works on all devices
- Smooth animations and transitions
- Professional typography with Google Fonts

## Troubleshooting

### Common Issues

1. **Port already in use:**
   - Backend: Change port in uvicorn command: `--port 8001`
   - Frontend: React will automatically suggest an alternative port

2. **Database issues:**
   - Delete `student_form.db` and restart the backend to recreate the database

3. **CORS errors:**
   - Ensure the backend is running on `http://localhost:8000`
   - Check that CORS middleware is properly configured

4. **Dependencies not found:**
   - Backend: Run `poetry install`
   - Frontend: Run `npm install`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
