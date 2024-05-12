from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routers import article_analysis_router


app = FastAPI()

app.include_router(article_analysis_router)

origins = ["http://localhost:3000"]  # Replace with your React frontend URL

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)

