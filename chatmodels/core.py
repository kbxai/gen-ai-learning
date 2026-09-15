from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()


class MovieInfo(BaseModel):
    title: Optional[str] = None
    release_year: Optional[int] = None
    genre: Optional[List[str]] = None
    director: Optional[str] = None
    cast: Optional[List[str]] = None
    imdb_rating: Optional[float] = None
    summary: Optional[str] = None
