from abc import ABC, abstractmethod

class IPredictionModelService(ABC):
    @abstractmethod
    async def predict(value1:float, value2:float) -> str:
        pass