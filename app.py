from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from markupsafe import Markup
import markdown
import os

# Загружаем .env файл
load_dotenv()

app = Flask(__name__)

# Берём ключ из переменных окружения
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
Ты — эксперт в законах и нормативных актах Республики Казахстан.

Требования к ответам:
1. Отвечай только по теме вопроса, без лишних отступлений.
2. Давай ответ максимально подробно, структурированно, но без "воды".
3. Обязательно используй пошаговую нумерацию или маркированные списки.
4. Выделяй важные слова или заголовки с помощью **жирного текста** (Markdown).
5. Если в ответе упоминаются законы, обязательно указывай их полное название и статью.
6. Не сокращай формулировки, чтобы человек без юридического образования тоже понял.
7. Не используй художественные или разговорные обороты, только деловой стиль.

Отвечай в формате Markdown, чтобы при отображении сохранялись переносы строк, списки и выделения.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3
        )

        raw_answer = response.choices[0].message.content
        html_answer = Markup(markdown.markdown(raw_answer))  # конвертируем Markdown в HTML
        return jsonify({"answer": html_answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
