from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev ke liye sab allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/config")
def get_config():
    return {
        "hero_title": "NeuralLearn – AI Powered EdTech",
        "hero_subtitle": "Backend is running successfully 🚀"
    }
