from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔐 CONFIG
BOT_TOKEN = "8692490877:AAHvz4SOORQlxDoK16nY3XgJctzmgDlU5yA"
CHAT_ID = "478503858"


def send_to_telegram(name, phone, order):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    message = f"""
🛒 NEW ORDER

👤 Name: {name}
📞 Phone: {phone}
🍕 Order: {order}

-------------------
"""

    try:
        response = requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": message
        })

        return response.status_code == 200

    except Exception as e:
        print("Telegram error:", e)
        return False


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        order = request.form.get("order")

        success = send_to_telegram(name, phone, order)

        return "<h2>✅ Order sent!</h2>" if success else "<h2>❌ Failed</h2>"

    return render_template("index.html")


if __name__ == "__main__":
    print("🚀 Running on http://127.0.0.1:5000")
    app.run(debug=True)