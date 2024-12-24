import unittest
from unittest.mock import patch, MagicMock
import pytest
from bot.handler.process_prompt import process_prompt
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


class TestBotHandlers(unittest.TestCase):
    # Модульные мок-тесты
    @patch('requests.post')
    @patch('telegram.Update')
    @patch('telegram.Message.reply_text')
    @patch('telegram.Message.chat.send_photo')
    @pytest.mark.asyncio
    async def test_process_prompt_success(self, mock_send_photo, mock_reply_text, mock_update, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"fake_image_data"
        mock_post.return_value = mock_response

        mock_update.message.text = "Generate image"
        mock_update.message.reply_text = mock_reply_text
        mock_update.message.chat.send_photo = mock_send_photo

        # Тестируем процесс
        await process_prompt(mock_update, None)

        mock_send_photo.assert_called_once_with(photo=b"fake_image_data")

    @patch('requests.post')
    @patch('telegram.Update')
    @patch('telegram.Message.reply_text')
    @pytest.mark.asyncio
    async def test_process_prompt_failure(self, mock_reply_text, mock_update, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        mock_update.message.text = "Generate image"
        mock_update.message.reply_text = mock_reply_text

        await process_prompt(mock_update, None)

        mock_reply_text.assert_called_once_with("Ошибка: {'detail': 'Internal Server Error'}")


if __name__ == "__main__":
    unittest.main()
