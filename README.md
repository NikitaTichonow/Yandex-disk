<h1 align="center">Yandex Disk Downloader</h1>
Этот проект представляет собой веб-приложение на Django, которое позволяет пользователям просматривать и загружать файлы из Яндекс.Диска по публичной ссылке. Приложение использует API Яндекс.Диска для получения списка файлов и предоставляет простой интерфейс для их загрузки.

<h2 align="center">Установка</h2>

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/NikitaTichonow/Yandex-disk

2. **Перейдите в папку проекта:**
    ```bash
    cd yandex_disk

3. **Установите виртуальное окружение и активируйте его:**
     ```bash
    python -m venv env
    source env/bin/activate   # Для Linux и macOS
    env\Scripts\activate      # Для Windows

4. **Установите необходимые зависимости:**
     ```bash
     pip install -r requirements.txt
   
5. **Откройте файл .env и заполнить его своими данными**
   ```env
    DJANGO_SECRET_KEY=your_django_secret_key
    YANDEX_DISK_API_TOKEN=your_yandex_disk_api_token

6. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    
7. **Доступ к приложению:**
   
    После завершения всех вышеуказанных шагов, приложение будет доступно по адресу http://127.0.0.1:8000.

