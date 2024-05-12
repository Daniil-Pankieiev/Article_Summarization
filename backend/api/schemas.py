from pydantic import BaseModel


class ArticleRequestSchema(BaseModel):
    text: str


class ArticleSummarySchema(BaseModel):
    summary: str
