from dependency_injector import containers, providers
from src.infrastructure.services.az_key_vault.KeyVaultManager import KeyVaultManager
from src.application.common.helpers.KeyVaultServices import KeyVaultServices
from src.api.config.Environment import get_environment_variables
from src.infrastructure.services.consume_service.ConsumeService import ConsumeService
from src.application.services.post.PostService import PostService
from src.infrastructure.services.prediction_model.PredictionModel import PredictionModel
from src.application.services.prediction.PredictionModelService import PredictionModelService

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    env = get_environment_variables()
    url_key_vault = env.AZURE_KEYVAULT_URL

    key_vault_manager = providers.Factory(
        KeyVaultManager,
        url= url_key_vault
    )

    key_vault_service = providers.Factory(
        KeyVaultServices,
        key_vault= key_vault_manager
    )

    consumer_service = providers.Factory(
        ConsumeService
    )

    post_service = providers.Factory(
        PostService,
        consume_service= consumer_service
    )

    prediction_model = providers.Factory(
        PredictionModel
    )

    prediction_service = providers.Factory(
        PredictionModelService,
        prediction_model = prediction_model
    )
