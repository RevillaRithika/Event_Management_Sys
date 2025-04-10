# Event Management System

A web-based event management system built with Flask and MySQL.

## Features

- Create, read, update, and delete events
- Manage event venues and organizers
- Track event attendees
- Modern and responsive user interface

## Prerequisites

- Python 3.7 or higher
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd event-management-system
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a MySQL database:
```sql
CREATE DATABASE event_management;
```

5. Configure the database connection:
   - Create a `.env` file in the project root
   - Add the following variables:
   ```
   DATABASE_URL=mysql+mysqlconnector://username:password@localhost/event_management
   SECRET_KEY=your-secret-key-here
   ```

6. Initialize the database:
```bash
python app.py
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
event-management-system/
├── app.py              # Main application file
├── config.py           # Configuration settings
├── models.py           # Database models
├── requirements.txt    # Python dependencies
├── static/            # Static files (CSS, JS)
│   └── style.css
├── templates/         # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── create_event.html
│   └── attendees.html
└── README.md
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 