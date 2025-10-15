from abc import ABC, abstractmethod

class IConsumeService(ABC):
    @abstractmethod
    async def get(self, url: str) -> str:
        pass

    @abstractmethod
    async def post(self, url:str, data: str) -> str:
        pass