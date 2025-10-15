from src.infrastructure.interfaces.IPredictionModel import IPredictionModel
from keras.models  import load_model
import os
from pathlib import Path

class PredictionModel(IPredictionModel):
    def __init__(self):        
        self.model_path = os.path.join('src', 'infrastructure', 'services', 'prediction_model', 'modelo_simple.h5')
        self.loaded_model = load_model(self.model_path)

    async def predict(self, value1:float, value2:float):
               
        input_list = [[value1, value2]]
        
        try:
            prediction = self.loaded_model.predict(input_list)
            is_true = prediction[0][0] >= 0.5
        except Exception as e:
            print(f"Error en la predicción: {str(e)}")
            is_true = value1 > value2
            
        return {"prediction": f"{is_true}"}