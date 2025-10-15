from abc import ABC, abstractmethod
from src.application.dtos.post.PostDto import PostDto

class IPostService(ABC):
    @abstractmethod
    async def get_post_by_id(self, id: int) -> PostDto:
        pass

    @abstractmethod
    async def create_post(self, post: PostDto) -> PostDto:
        pass