from DeeperSeek import DeepSeek
from config import DeepSeekConfig


class Glados:
    api: DeepSeek
    _is_initialized: bool

    def __init__(self) -> None:
        self._is_initialized = False
        configs = DeepSeekConfig()  # type: ignore
        self.api = DeepSeek(
            email=configs.email,
            password=configs.password,
            verbose=False,
            headless=configs.headless,
            attempt_cf_bypass=True,
            chat_id=configs.chat_id,
            token=configs.ai_token,
        )

    async def __initialize(self) -> None:
        await self.api.initialize()
        self._is_initialized = True

    async def get_answer(self, text: str) -> str | None:
        if not self._is_initialized:
            await self.__initialize()
        response = await self.api.send_message(
            message=(
                "Ты комментируешь посты роботехнического клуба Robotic от имени "
                "Glados из игры Portal. Отвечай на русском и без лишних слов. "
                "Строго ответ от имени Glados. Сохрани ее язвительность и характер"
                "Текст поста:"
                '"' + text + '"'
            ),
            deepthink=False,
            search=False, 
            slow_mode=False,
            slow_mode_delay=0.25,
            timeout=60,
        ) 

        if response:
            return response.text
        else:
            return None
