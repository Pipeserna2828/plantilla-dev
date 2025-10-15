from fastapi import status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.application.common.exceptions.BusinessException import BusinessException

class ExceptionHandler():
   
    async def business_exception_handler(request: Request, exc: BusinessException):
        print(f"Business Exception: {exc.name}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"Title" : "Business Exception", "Error":  exc.name },
        )

    async def exception_handler(request: Request, exc: Exception):
        print(f"OMG! An HTTP error!: {repr(exc)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"Title" : "Unhandled Error", "Error":  "An error occurred while processing your request." },
        )

    async def validation_exception_handler(request: Request, exc: RequestValidationError): 
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content= {"Title" : "BadRequest", "Error":  exc.errors() },
        )