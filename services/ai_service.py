import google.generativeai as genai

from core.config import settings


genai.configure(
    api_key=settings.GEMINI_API_KEY
)


class AIService:

    def __init__(self):

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(
        self,
        prompt
    ):

        response = (
            self.model
            .generate_content(
                prompt
            )
        )

        return response.text