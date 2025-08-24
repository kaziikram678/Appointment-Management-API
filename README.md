📅 Appointment Management API

A FastAPI + SQLite based RESTful API for managing patients and their appointments.
Built with FastAPI, SQLAlchemy ORM, and Pydantic, and deployed on a free cloud platform (Railway/Render).


 ✨ Features

* 🧑‍⚕️ Patients Management – Store patient details (name, email, phone).
* 📆 Appointments Management – Book, retrieve, and manage appointments linked to patients.
* 💾 SQLite Database – Lightweight relational database for persistent storage.
* ✅ Data Validation – Powered by Pydantic for clean request/response handling.
* 🚀 Cloud Deployment – Easily deployed on free hosting services like Railway or Render.



 🛠️ Tech Stack

* Backend: [FastAPI](https://fastapi.tiangolo.com/)
* Database: SQLite (via SQLAlchemy ORM)
* Validation: Pydantic
* Deployment: Railway / Render



 ⚙️ Installation & Setup

 1. Clone the repository

```bash
git clone https://github.com/your-username/appointment-management-api.git
cd appointment-management-api
```

 2. Create virtual environment & install dependencies

```bash
python -m venv env
source env/bin/activate    On Windows: env\Scripts\activate
pip install -r requirements.txt
```

 3. Run the server

```bash
uvicorn main:app --reload --port 5000
```

Server will be running at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)



 📖 API Endpoints

 Patients

* `POST /patients/` → Create a new patient
* `GET /patients/` → Retrieve all patients

 Appointments

* `POST /appointments/` → Create a new appointment
* `GET /appointments/` → Retrieve all appointments



 📦 Project Structure

```
.
├── app/
│   ├── database.py        SQLite DB setup with SQLAlchemy
│   ├── models.py          Database models (Patient, Appointment)
│   ├── schemas.py         Pydantic schemas for validation
│   ├── routes.py          API routes (patients + appointments)
│   └── __init__.py
├── main.py                FastAPI entry point
├── requirements.txt       Dependencies
└── README.md              Project docs
```



 🌍 Deployment

This project can be deployed for free using services like:

* [Railway](https://railway.app/)
* [Render](https://render.com/)
* [Heroku](https://www.heroku.com/)



 📌 Future Improvements

* Update & Delete endpoints for patients and appointments
* Authentication & role-based access control
* Docker support for easier deployment



 👨‍💻 Author

Your Name

* GitHub: [](https://github.com/kaziikram678)
* LinkedIn: [](https://www.linkedin.com/in/md-ikram-ab515618b/)

