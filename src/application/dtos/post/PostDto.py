from pydantic import BaseModel

class PostDto(BaseModel):
    userId: int
    id: int
    title: str
    body: str