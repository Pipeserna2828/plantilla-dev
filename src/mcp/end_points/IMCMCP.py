from fastapi import APIRouter

class IMCMCP:

    routerPostMCP = APIRouter()
    
    @routerPostMCP.get( "/imc" , operation_id= "calculate_imc" , summary= "esta herramienta se utiliza para calcular el IMC en función del peso y la altura" )
    def  calculate_imc ( weight_kg: float , height_m: float ): 
        return { "imc" : weight_kg / (height_m ** 2 )}