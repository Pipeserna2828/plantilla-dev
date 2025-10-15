from abc import ABC, abstractmethod

class IPredictionModel(ABC):
    @abstractmethod
    async def predict(value1:float, value2:float) -> str:
        pass


