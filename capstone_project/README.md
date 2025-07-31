# 🌿 Urban Green Space Access Analyzer

A data-driven web application that calculates Green Equity Scores and visualizes green space access across Miami-Dade County.

## 📁 Project Structure

- `/frontend` — React frontend (from fenago21 template)
- `/backend/api` — FastAPI backend
- `/backend/etl` — ETL scripts for merging environmental and demographic data
- `/data` — Source and processed datasets

## ▶️ Run Backend
```bash
cd backend
uvicorn api.main:app --reload
```

## ▶️ Run ETL
```bash
cd backend
python etl/pipeline.py
```

## 🌐 Deployment
- Frontend: Vercel
- Backend: Render