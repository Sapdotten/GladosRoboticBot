# Бот для канала клуба Robotic


## Описание
Данный репозиторий представляет собой исходный код для telegram-бота, задачей которого является комментировать посты в канале робототехнического клуба Robotic от имени Glados из игры Portal.

Пока что бот комментирует комментарии посты только одного заданного канала и ориентируется на текст поста. На пересланные сообщения он не реагирует.
### Запланированные доработки:
- [ ] Доработать DeeperSeek или заменить на другое API, т.к. иногда бот не проходит капчу от Claudflare.

## Развертывание и запуск
### Переменные окружения

| Переменная | Тип | Описание
|----------|----------|---------
| BOT_TOKEN | string   | Токен доступа к tg-боту
| BOT_CHANNEL_ID | string  | ID tg-канала
| AI_EMAIL | string | почта от аккаунта deepseek
| AI_PASSWORD | string | пароль от аккаунта deepseek
| AI_CHAT_ID | string | id чата deepseek
| AI_TOKEN | string | токен от акканута deepseek. [Инструкция по получению](https://github.com/Sapdotten/DeeperSeek/tree/main/docs#obtaining-the-session-token)
| AI_HEADLESS | bool | По умолчанию `true`. Если `false`, то для deepseek будет открываться браузер.

### Запуск
```sh
docker build -t glados .
docker run -d glados
```

## О клубе
Клуб **ROBOTIC** — это студенческое объединение *Самарского университета*. Мы занимаемся робототехникой, программированием, электроникой и 3D-моделированием. Открыты для всех, кто хочет развиваться и участвовать в технических проектах.

VK: [https://vk.com/robotic_samara](https://vk.com/robotic_samara)

TG: [t.me/robotic_samara](t.me/robotic_samara)
