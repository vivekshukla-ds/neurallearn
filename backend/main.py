from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage (abhi simple rakhenge)
ARTICLES = []

@app.get("/config")
def config():
    return {
        "status": "ok",
        "message": "Backend is running successfully 🚀"
    }

@app.get("/articles")
def get_articles():
    return ARTICLES

@app.post("/publish")
def publish_article(article: dict):
    ARTICLES.append(article)
    return {
        "status": "published",
        "total": len(ARTICLES)
    }
