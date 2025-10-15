from src.application.interfaces.IKeyVaultServices import IPostService
from src.infrastructure.interfaces.IKeyVaultManager import IKeyVaultManager

class KeyVaultServices(IPostService):

    def __init__(self, key_vault: IKeyVaultManager):
        self.key_vault = key_vault

    def read_secret(self, secret_name: str):
        secret_value = self.key_vault.get_secret(secret_name)
        return secret_value
    