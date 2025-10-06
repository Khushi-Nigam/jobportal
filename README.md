<!-- Shields/Badges for quick project info -->
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-4.2-green" alt="Django Version">
  </a>
  <a href="https://github.com/yourusername/DreamJobs/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
  </a>
  <a href="https://dreamjobs-9pmg.onrender.com/">
    <img src="https://img.shields.io/badge/Live-Demo-brightgreen" alt="Live Demo">
  </a>
</p>

<!-- Logo & Title -->
<h1 align="center">🚀 DreamJobs - Where Dreams Meet Careers!</h1>

<p align="center">
  A full-featured job portal built with Django, connecting talented job seekers with top employers.
  <br>
  <a href="https://dreamjobs-9pmg.onrender.com/"><strong>Explore the Live Site »</strong></a>
  <br>
  <a href="#getting-started">View Setup</a>
  ·
  <a href="#key-features">View Features</a>
  ·
  <a href="#contributing">Contribute</a>
</p>

---
## 🌟GSSoc 
![GSSoC Logo](https://github.com/dimpal-yadav/jobportal/blob/add-gssoc-banner/GSSoC.png)
🌟 **Exciting News...**

🚀 This project is now an official part of GirlScript Summer of Code – GSSoC'25! 💃🎉💻 We're thrilled to welcome contributors from all over India and beyond to collaborate, build, and grow *jobportal!* Let’s make learning and career development smarter – together! 🌟👨‍💻👩‍💻

👩‍💻 GSSoC is one of India’s **largest 3-month-long open-source programs** that encourages developers of all levels to contribute to real-world projects 🌍 while learning, collaborating, and growing together. 🌱

🌈 With **mentorship, community support**, and **collaborative coding**, it's the perfect platform for developers to:

- ✨ Improve their skills
- 🤝 Contribute to impactful projects
- 🏆 Get recognized for their work
- 📜 Receive certificates and swag!

🎉 **I can’t wait to welcome new contributors** from GSSoC 2025 to this jobportal project family! Let's build, learn, and grow together — one commit at a time. 🔥👨‍💻👩‍💻

---

## ✨ Quick Preview

### 🧑‍💼 Job Seeker Experience
| Browse Jobs & Apply | Personalized Dashboard |
|:---:|:---:|
| ![Job Seeker - Browse and Apply](https://via.placeholder.com/500x300/4A90E2/FFFFFF?text=GIF+1:+Browse+Jobs+%26+Apply) | ![Job Seeker - Dashboard](https://via.placeholder.com/500x300/50BBA0/FFFFFF?text=GIF+2:+Job+Seeker+Dashboard) |

*GIFs showing a user searching for jobs, filtering results, and submitting an application, then managing their applications from their dashboard.*

### 👔 Employer Experience
| Post a New Job | Manage Applicants |
|:---:|:---:|
| ![Employer - Post Job](https://via.placeholder.com/500x300/F5A623/FFFFFF?text=GIF+3:+Post+New+Job) | ![Employer - Manage Applicants](https://via.placeholder.com/500x300/D0021B/FFFFFF?text=GIF+4:+Manage+Applicants) |

*GIFs showing a recruiter creating a new job posting and then reviewing, shortlisting, or rejecting candidates from their dashboard.*

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### ✅ Prerequisites

Before you begin, ensure you have the following installed:
- **Python** (3.8 or higher) - [Download here](https://www.python.org/downloads/)
- **Git** - [Download here](https://git-scm.com/)
- **Pip** (Python package manager, usually comes with Python)

### ⚙️ Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/DreamJobs.git
   cd DreamJobs
Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate


# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Your command prompt should now show (venv) at the beginning.
```

Install Dependencies

```bash
pip install -r requirements.txt
Set Up the Database
```

```bash
python manage.py makemigrations
python manage.py migrate
```
(Optional) Create a Superuser for Admin Access

```bash
python manage.py createsuperuser
```
- Follow the prompts to create an admin account. This is useful for accessing the Django admin panel.

- Run the Development Server

```bash
python manage.py runserver
```
🎉 You're All Set!
Open your web browser and go to:

```
Main Application: http://127.0.0.1:8000

Admin Panel: http://127.0.0.1:8000/admin (if you created a superuser)
```
<img width="1919" height="1075" alt="image" src="https://github.com/user-attachments/assets/6e7b976f-625a-4264-abd9-9888f29c0cca" />


##  🗂️ File Structure

```
jobportal/
|
├── adminapp/
│   ├── migrations/
│   ├── static/assets/
│   ├── templates/
│   └── __init__.py, admin.py, adminappurrls.py, apps.py, models.py, tests.py, views.py
|
├── employer/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   └── Procfile, __init__.py, admin.py,apps.py, employerurls.py,  models.py, tests.py, views.py
|
├── jobapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   └── __init__.py, admin.py, apps.py, jobappurls.py, models.py, tests.py, views.py
|
├── jsapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   └── __init__.py, admin.py, apps.py,jsappurls.py, models.py, tests.py, views.py
|
├── jobportal/  # root config
│   └── settings.py, urls.py, ...
|
├── media/
│   └── *avif / *.jpg / *.png / *.webp
|
├── staticfiles/
|   ├── admin/
│   ├── assets/
│   ├── css/
|   ├── images/
│   ├── js/
│   └── *.jpg / *mp4 / *.png / *.svg / *.webp
|
├── README.md
├── db.sqlite3
├── manage.py
└── requirements.txt
```
# ✨ Key Features
# For Job Seekers
- 🔍 Smart Job Search: Filter by location, industry, and experience level.
- 📄 One-Click Applications: Save your resume and apply to jobs effortlessly.

- 📊 Application Tracker: Monitor the status of every application you submit.

- 👤 Personalized Dashboard: Manage your profile and view recommended jobs.

# For Employers
- 📢 Easy Job Posting: Create and publish new job vacancies in minutes.

- 👥 Applicant Management System: View, shortlist, and manage all applicants from a central dashboard.

- 🔎 Talent Discovery: Search for candidates based on skills and experience.

# For Everyone
- 🔐 Secure Authentication: Separate login systems for job seekers and employers.

- 📱 Fully Responsive: Seamless experience on desktop, tablet, and mobile devices.

# 🛠️ Technologies Used
Layer	Technologies
- Frontend : 	HTML, CSS, JavaScript, Bootstrap
- Backend	: Python, Django
- Database :	SQLite (Development)
- Deployment	Render
# 🤝 Contributing
- We love your input! We want to make contributing to DreamJobs as easy and transparent as possible.

- If you have a suggestion, bug report, or want to add a new feature, please check out our Contributing Guide for details on our code of conduct and the process for submitting pull requests.

- First time contributing? No problem! Look for issues labeled good first issue to get started.

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

A heartfelt thank you to all the contributors who have dedicated their time and effort to make this project a success.  
Your contributions—whether it’s code, design, testing, or documentation—are truly appreciated! 🚀

#### Thanks to all the wonderful contributors 💖

<a href="https://github.com/Khushi-Nigam/jobportal/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Khushi-Nigam/jobportal" />
</a>


<p align="center"> <a href="#top" style="font-size: 16px; padding: 10px 20px; display: inline-block; border: 1px solid #ccc; border-radius: 6px; text-decoration: none; color: #333;"> ⬆️ Back to Top </a> </p> ```
