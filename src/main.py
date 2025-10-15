from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from src.api.end_points.PostEndPoint import PostEndPoint
from src.api.end_points.PredictionModelEndPoint import PredictionModelEndPoint
from src.application.common.exceptions.BusinessException import BusinessException
from src.api.exception_handler import ExceptionHandler
from src.api.exception_handler.ExceptionHandler import ExceptionHandler
from src.mcp.end_points.IMCMCP import IMCMCP
from fastapi_mcp import FastApiMCP 
from src.api.config.Environment import get_environment_variables
env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)

app.include_router(PostEndPoint.routerPost, prefix="/post", tags=["Post"])
app.include_router(PredictionModelEndPoint.routerPredictionModel, prefix="/prediction", tags=["Prediction"])
app.include_router(IMCMCP.routerPostMCP, prefix="/mcp", tags=["MCP"])
mcp = FastApiMCP(app, name= "BMI MCP" , description= "Aplicación sencilla para calcular el IMC" ) 
mcp.mount()

app.add_exception_handler(BusinessException, ExceptionHandler.business_exception_handler)
app.add_exception_handler(Exception, ExceptionHandler.exception_handler)
app.add_exception_handler(RequestValidationError, ExceptionHandler.validation_exception_handler)