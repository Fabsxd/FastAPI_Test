# 💊 Hospital Medication Tracking API

> _"Helping hospitals stay one step ahead of their medications."_

Welcome to the Hospital Medication Tracking API — a fast, reliable backend built with **FastAPI** and **PostgreSQL** to manage how medicines are prescribed, tracked, and monitored for hospital patients.

This project isn't just CRUD — it's an effort to bring clarity to the medical backend world, with automation, logic-based scheduling, and solid data relationships under the hood.

---

## 🚀 What This API Does

✅ Manage patient records  
✅ Track medicine inventory and restock needs  
✅ Schedule and monitor prescriptions  
✅ Register emergency treatments  
✅ Automate purchase lists when stock is low  
✅ Perform fast queries for reporting and operations

---

## ⚙️ Tech Stack

- **Python + FastAPI** – For blazing fast, modern backend endpoints  
- **PostgreSQL + SQLAlchemy** – Robust and scalable relational database  
- **Docker** – For containerized deployments (Azure-ready)  
- **Pydantic** – Data validation made elegant  
- **Structured Schema & Views** – Optimized queries for performance

---

## 🌐 Endpoints Overview

| Method | Endpoint                  | Description                            |
|--------|---------------------------|----------------------------------------|
| GET    | `/patient/{id}`           | Fetch patient data                     |
| POST   | `/patient/`               | Register a new patient                 |
| PUT    | `/patient/{id}`           | Update full patient record             |
| PATCH  | `/patient/{id}`           | Partially update patient info          |
| GET    | `/medicines/low-stock`    | View all low-stock medicines           |
| POST   | `/emergency/`             | Record emergency prescription          |

> **More endpoints coming soon** for medicine management and prescription logic.

---

## 📊 Database Highlights

- **7 interconnected tables**
- **3 optimized views**
- **Indexed for frequent searches**
- **Trigger-based purchase list automation**

> Want to see how it all connects? Check out the `design.md` and schema in `/docs`.

---

## 🧠 What This Project Is Really About

This isn’t a final product — it’s a foundation. The goal is to **practice clean architecture, real-world data modeling**, and work with tools that scale.

I built this project not because I knew how, but because I **wanted to understand how it’s really done**.  
There’s still a lot to learn — and that’s the whole point. 🚧

---

## 📹 Walkthrough Video

Watch the full project walkthrough 👉 [Click here](https://drive.google.com/file/d/1JPVCLzLLGNRuArwdgx-dK2cNcUy3QbU_/view?usp=sharing)

---

## 📬 Contact

Have feedback, ideas, or looking to collaborate?  
Reach out via [LinkedIn](https://www.linkedin.com/in/yourprofile) or open an issue — I’m always open to improvement and real-world challenges.

---

## ⚡️ Final Thoughts

> "Code that works is good. Code that grows with you is better."

If this API inspires you, helps you, or makes you think “this guy’s going somewhere,” then mission accomplished.  
This is just the start. More projects and polish to come.

---

**Thanks for reading. Let’s build better backends.**
