from fastapi import APIRouter
from src.application.dtos.post.PostDto import PostDto
from src.api.config.Containers import Container

container = Container()

class PostEndPoint:

    routerPost = APIRouter()
  
    @routerPost.get("/{id}/user")
    async def get_post_by_id(id:int):
        result = await container.post_service().get_post_by_id(id)
        return result
    
    @routerPost.post("", response_model=PostDto, responses={200: {"description": "Successful Response"}})
    async def create_post(post:PostDto):
        result = await container.post_service().create_post(post)
        return result
    
    
    