from src.infrastructure.interfaces.IConsumeService import IConsumeService
from src.application.interfaces.IPostService import IPostService
from src.api.config.Environment import get_environment_variables
from src.application.dtos.post.PostDto import PostDto
from src.application.common.exceptions.ExceptionService import ExceptionService
import json

class PostService(IPostService):
    
    def __init__(self, consume_service : IConsumeService):
        self.consume_service = consume_service
        self.env = get_environment_variables()

    async def get_post_by_id(self, id: int)->PostDto:
        result = await self.consume_service.get(f"{self.env.URL_POST}/{id}")
        if result is None:
            raise ExceptionService("error al realizar la consulta")
        json_result = json.loads(result)
        return PostDto(**json_result)
    
    async def create_post(self, post: PostDto) -> PostDto:
        data = post.dict()
        result = await self.consume_service.post(self.env.URL_POST, data)
        if result is None:
            raise ExceptionService("error al crear el post")
        json_result = json.loads(result)        
        return PostDto(**json_result)