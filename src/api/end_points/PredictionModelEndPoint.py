from fastapi import APIRouter
from src.api.config.Containers import Container

container = Container()

class PredictionModelEndPoint:

    routerPredictionModel = APIRouter()
    
    @routerPredictionModel.post("")
    async def prediction_model(value1:float, value2:float):
        result = await container.prediction_service().predict(value1,value2)
        
        return result
    
    
    