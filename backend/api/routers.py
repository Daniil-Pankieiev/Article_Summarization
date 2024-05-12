from fastapi import APIRouter

from backend.api.crud import ArticleAnalysisCRUD
from backend.api.schemas import ArticleRequestSchema, ArticleSummarySchema

article_analysis_router = APIRouter()


@article_analysis_router.post("/summarize", response_model=ArticleSummarySchema)
async def summarize_article(article: ArticleRequestSchema):
    return await ArticleAnalysisCRUD.summarize_text(article)
