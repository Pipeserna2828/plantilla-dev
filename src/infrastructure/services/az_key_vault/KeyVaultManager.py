from azure.identity import DefaultAzureCredential, AzureCliCredential
from azure.keyvault.secrets import SecretClient
import os
from src.infrastructure.interfaces.IKeyVaultManager import IKeyVaultManager

class KeyVaultManager(IKeyVaultManager):

    def __init__(self, url: str):
       
        if os.getenv("ENV") == "local":
            self.credential = AzureCliCredential() 
            self.vault_url = url
        else:
            self.credential = DefaultAzureCredential() 
            self.vault_url = url

        self.client = SecretClient(vault_url=self.vault_url, credential=self.credential)

    def get_secret(self, secret_name: str) -> str:
        secret = self.client.get_secret(secret_name).value
        return secret
