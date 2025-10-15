import httpx
from src.infrastructure.interfaces.IConsumeService import IConsumeService

class ConsumeService(IConsumeService):
    def __init__(self):
        self.client = httpx.AsyncClient()
        
    async def get(self, url:str):
        response = await self.client.get(url)
        if response.status_code == httpx.codes.OK:
            return response.content.decode('utf-8')
        else:
            return None
        
    async def post(self,url:str, data:str):
        response = await self.client.post(url,json=data)
        if response.status_code == httpx.codes.CREATED:            
            return response.content.decode('utf-8')
        else:
            return None
            