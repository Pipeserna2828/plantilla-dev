import pytest
from unittest.mock import Mock
from src.application.common.helpers.KeyVaultServices import KeyVaultServices
from src.infrastructure.interfaces.IKeyVaultManager import IKeyVaultManager

@pytest.fixture
def mock_key_vault():
    return Mock(IKeyVaultManager)

@pytest.fixture
def key_vault_services(mock_key_vault):
    return KeyVaultServices(mock_key_vault)

class TestUnitKeyVaultServices:

    def test_read_secret_returns_secret_value(self, mock_key_vault, key_vault_services):
        # Arrange
        secret_name = "my-secret"
        expected_secret_value = "my-secret-value"
        mock_key_vault.get_secret.return_value = expected_secret_value
        service = key_vault_services

        # Act
        result = service.read_secret(secret_name)

        # Assert
        assert result == expected_secret_value