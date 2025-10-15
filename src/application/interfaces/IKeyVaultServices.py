from abc import ABC, abstractmethod

class IPostService(ABC):
    
    @abstractmethod
    def read_secret(self, secret_name: str) -> str:
        pass