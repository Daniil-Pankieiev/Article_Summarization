import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

from backend.api import settings

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


async def generate_summary(text) -> str:
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
    vertexai.init(project=settings.PROJECT_NAME, location=settings.LOCATION)
    model = GenerativeModel(settings.MODEL_NAME)
    responses = await model.generate_content_async(
        [
            f"""As a professional summarizer, create a concise and comprehensive summary
     of the provided text, be it an article, post, conversation, or passage,
     while adhering to these guidelines: * Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness. * Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects. * Rely strictly on the provided text, without including external information. * Format the summary in paragraph form for easy understanding. * Your output, result must be in the  language of the provided text. * Result maximum 100 words

    input: {text}
    output:
    """
        ],
        generation_config=settings.generation_config,
        safety_settings=safety_settings,
    )
    return responses.text
