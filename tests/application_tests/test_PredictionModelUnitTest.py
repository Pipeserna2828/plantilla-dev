import pytest
from unittest.mock import Mock, AsyncMock
from src.application.services.prediction.PredictionModelService import PredictionModelService
from src.application.interfaces.IPredictionModelService import IPredictionModelService

@pytest.fixture
def mock_prediction_model():
    return Mock(IPredictionModelService)

@pytest.fixture
def prediction_model_service(mock_prediction_model):
    return PredictionModelService(mock_prediction_model)

class TestUnitPredictionModel:

    @pytest.mark.asyncio
    async def test_predict_returns_expected_result(self, mock_prediction_model, prediction_model_service):
        # Arrange
        mock_prediction_model.predict = AsyncMock(return_value=0.3)
        service = prediction_model_service

        # Act
        result = await service.predict(1.0, 2.0)

        # Assert
        assert result == 0.3