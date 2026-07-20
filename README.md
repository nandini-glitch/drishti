# Drishti: AI-Driven Supply Chain Resilience

**Drishti** (Sanskrit for "Vision") is an AI-powered supply chain digital twin and predictive risk orchestration platform. It continuously ingests global geopolitical intelligence to anticipate supply chain shocks before they cascade into critical disruptions.

![Drishti Dashboard](https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/eye.svg)

## 🏆 Hackathon Overview
Built as a highly technical, end-to-end hackathon solution, Drishti tackles global energy and logistics supply chain vulnerabilities. By mapping global crude oil corridors, refineries, and Strategic Petroleum Reserves (SPR), the platform mathematically mitigates risk in real-time.

## 🚀 Key Features

1. **Geopolitical Risk Intelligence Agent:** Live ingestion of global news feeds (via Tinyfish AI) parsed by Gemini LLMs to extract entity sanctions and crisis severities. Fuses with real-time AIS shipping density and commodity pricing.
2. **Supply Chain Digital Twin:** A beautiful Material Design 3 cinematic dashboard powered by MapLibre GL and WebGL. Map nodes dynamically glow and shift from green to red based on live AI disruption scores.
3. **Disruption Scenario Modeller:** Quantifies unmitigated supply gaps into macroeconomic metrics, instantaneously projecting fuel price spikes and GDP drag impacts.
4. **Adaptive Procurement Orchestrator:** Instantly ranks and recommends alternative global crude sources to bridge supply gaps, optimizing for API Gravity compatibility, Sulfur content, transit time, and landed cost.
5. **Strategic Reserve Optimisation:** Mathematically projects Strategic Petroleum Reserve (SPR) volumetric drawdown schedules necessary to sustain refineries until adaptive procurement shipments arrive.

## 🛠️ Technology Stack

**Frontend:**
- Next.js 15 (React 19)
- TypeScript
- Framer Motion (Micro-animations)
- MapLibre GL JS / react-map-gl (Digital Twin)
- Material Design 3 (M3) CSS Architecture

**Backend:**
- FastAPI (Python)
- Supabase (PostgreSQL + pgvector)
- Tinyfish AI API (Intelligence Ingestion)
- Google Gemini (NLP Entity & Severity Extraction)

## ⚙️ Local Development

### 1. Database Setup (Supabase)
Run the SQL scripts in the `backend/supabase` folder inside your Supabase SQL Editor to generate the schema and seed the initial supply chain baseline data.

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Create a `.env` file with your `SUPABASE_URL`, `SUPABASE_KEY`, `GEMINI_API_KEY`, `TINYFISH_API_KEY`, and `INGEST_SECRET`.
```bash
python -m uvicorn src.app:app --port 8080 --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```
Create a `.env.local` file with `NEXT_PUBLIC_MAPTILER_KEY` and `NEXT_PUBLIC_API_URL=http://127.0.0.1:8080`.
```bash
npm run dev
```

## 🌐 Live Demo
- **Frontend:** [https://drishti-navy.vercel.app/](https://drishti-navy.vercel.app/)
- **Backend API:** [https://drishti-on9a.onrender.com](https://drishti-on9a.onrender.com)
