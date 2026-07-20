from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import ingest, risk, actions, twin

app = FastAPI(title="Drishti API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router)
app.include_router(risk.router)
app.include_router(actions.router)
app.include_router(twin.router)


@app.get("/health")
def health():
    return {"status": "ok"}
