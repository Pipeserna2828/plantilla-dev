from abc import ABC, abstractmethod

class IKeyVaultManager(ABC):
    @abstractmethod
    def get_secret(self, secret_name: str) -> str:
        pass