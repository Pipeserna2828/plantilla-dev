
import pytest
import json
from unittest.mock import AsyncMock, MagicMock
from src.application.services.post.PostService import PostService
from src.infrastructure.interfaces.IConsumeService import IConsumeService
from src.application.dtos.post.PostDto import PostDto

@pytest.fixture
def mock_consume_service():
    return AsyncMock(spec=IConsumeService)

@pytest.fixture
def post_service(mock_consume_service):
    return PostService(mock_consume_service)

class TestUnitsPostUnit:

    @pytest.mark.asyncio
    async def test_get_post_by_id_returns_post(self, mock_consume_service, post_service):
        # Arrange
        expected_post_data = {
            "userId": 1,
            "id": 1,
            "title": "Test Post",
            "body": "This is a test post."
        }
        mock_consume_service.get.return_value = json.dumps(expected_post_data)

        # Act
        result = await post_service.get_post_by_id(1)

        # Assert
        assert isinstance(result, PostDto)
        assert result.id == 1
        assert result.title == "Test Post"
        assert result.body == "This is a test post."

    @pytest.mark.asyncio
    async def test_create_post_returns_created_post(self, mock_consume_service, post_service):
        # Arrange
        input_post = PostDto(userId=1, id=1, title="New Post", body="This is a new post.")
        expected_created_post_data = {
            "userId": 1,
            "id": 2,
            "title": "New Post",
            "body": "This is a new post."
        }
        mock_consume_service.post.return_value = json.dumps(expected_created_post_data)

        # Act
        created_post = await post_service.create_post(input_post)

        # Assert
        assert isinstance(created_post, PostDto)
        assert created_post.id == 2
        assert created_post.title == "New Post"
        assert created_post.body == "This is a new post."