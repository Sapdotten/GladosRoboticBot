# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app
RUN apt update && apt install -y \
    git \
    wget \
    chromium \
    chromium-driver \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    xvfb \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все содержимое текущей директории в рабочую директорию контейнера
COPY . .


# Копируем файл .env
#COPY .env ./app/.env

CMD ["python3", "src/main.py"]