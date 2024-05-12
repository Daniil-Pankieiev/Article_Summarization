from fastapi import HTTPException

from backend.api.schemas import ArticleRequestSchema, ArticleSummarySchema
from backend.api.utils import generate_summary


class ArticleAnalysisCRUD:
    @staticmethod
    async def summarize_text(article: ArticleRequestSchema) -> ArticleSummarySchema:
        """
           This function generates a summary of the provided text using the Vertex AI generative model.

           The function initializes the Vertex AI with the project and location settings, then creates a generative model
           using the model name from the settings. It then generates content asynchronously using the model, with a specific
           prompt and safety settings.

           The prompt instructs the model to create a concise and comprehensive summary of the provided text, adhering to
           certain guidelines such as crafting a detailed, thorough, in-depth, and complex summary while maintaining clarity
           and conciseness, incorporating main ideas and essential information, eliminating extraneous language and focusing
           on critical aspects, relying strictly on the provided text, without including external information, formatting the
           summary in paragraph form for easy understanding, and ensuring the output is in the language of the provided text
           and does not exceed 100 words.

           The function returns the text of the generated responses.

           Args:
               text (str): The text to be summarized.

           Returns:
               str: The generated summary of the provided text.
           """
        try:
            summary = await generate_summary(article.text)
            return ArticleSummarySchema(summary=summary)
        except Exception as e:
            # Handle specific exceptions or generic ones
            # Raise a more informative HTTPException for the route
            raise HTTPException(
                status_code=500, detail=f"Error generating summary: {str(e)}"
            )
