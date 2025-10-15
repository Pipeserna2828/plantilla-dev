from src.infrastructure.interfaces.IPredictionModel import IPredictionModel
from src.application.interfaces.IPredictionModelService import IPredictionModelService


class PredictionModelService(IPredictionModelService):

    def __init__(self, prediction_model : IPredictionModel):
        self.prediction_model = prediction_model

    async def predict(self, value1:float, value2:float):
        
        prediction = await self.prediction_model.predict(value1, value2)

        return prediction