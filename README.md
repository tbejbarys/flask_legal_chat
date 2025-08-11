# 💬 Flask Legal Chat — Чат-бот по законам Казахстана

Этот проект — веб-приложение на Flask, которое позволяет пользователям задавать вопросы о законах Республики Казахстан и получать **подробные, структурированные и точные** ответы.  
Чат-бот использует OpenAI API для генерации ответов в формате Markdown, а на фронтенде поддерживает тёмную/светлую темы, анимацию появления сообщений и индикатор «Бот печатает…».

---

## 🚀 Функционал
- 📜 **Подробные юридические ответы** — бот структурирует информацию, использует нумерацию и ссылки на статьи законов.
- 🎨 **Современный интерфейс** на Bootstrap 5.
- 🌗 **Тёмная и светлая тема** с переключением.
- ⌨️ **Отправка сообщений по клавише Enter**.
- ✨ **Анимация появления сообщений** и индикатор набора текста.
- 🖋 **Поддержка Markdown** — жирный текст, списки, заголовки.

---

## 🛠 Стек технологий
- **Backend:** [Flask](https://flask.palletsprojects.com/), [OpenAI API](https://platform.openai.com/)
- **Frontend:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/)
- **Прочее:** [Markdown](https://python-markdown.github.io/) для форматирования ответов

---

## 📦 Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/username/flask-legal-chat.git
cd flask-legal-chat
```

### 2. Создать виртуальное окружение

```bash
python -m venv myenv
```

### 3. Активировать окружение

* **Windows**

```bash
myenv\Scripts\activate
```

* **MacOS / Linux**

```bash
source myenv/bin/activate
```

### 4. Установить зависимости

```bash
python -m pip install -r requirements.txt
```

### 5. Указать API-ключ

В файле `.env` (создать в корне проекта):

```env
OPENAI_API_KEY=ваш_api_ключ
```

### 6. Запустить сервер

```bash
python app.py
```

### 7. Открыть в браузере

```
http://127.0.0.1:5000
```

---

## 📂 Структура проекта

```
flask_legal_chat/
│
├── static/
│   └── style.css        # Стили фронтенда
│
├── templates/
│   └── index.html       # HTML интерфейс
│
├── app.py               # Основная логика Flask
├── requirements.txt     # Список зависимостей
├── README.md            # Описание проекта
└── .env                 # API-ключ OpenAI
```
