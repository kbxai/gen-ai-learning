import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()


class MovieInfo(BaseModel):
    title: Optional[str] = None
    release_year: Optional[int] = None
    genre: Optional[List[str]] = None
    director: Optional[str] = None
    cast: Optional[List[str]] = None
    imdb_rating: Optional[float] = None
    summary: Optional[str] = None


parser = PydanticOutputParser(pydantic_object=MovieInfo)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Extract movie information from the paragraph.

{format_instructions}"""
    ),
    (
        "human",
        "{text}"
    )
])


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


# Streamlit UI
st.title("Movie Information Extractor")

para = st.text_area(
    "Enter the movie-related text:",
    height=250
)


if st.button("Extract Information"):
    if para:

        final_prompt = prompt.format_prompt(
            text=para,
            format_instructions=parser.get_format_instructions()
        ).to_string()

        response = model.invoke(final_prompt)

        result = parser.parse(response.content[0]["text"])

        st.write(result)
