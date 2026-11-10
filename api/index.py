from flask import Flask, request
import os

app = Flask(__name__)

# আপনার বটের টোকেন এবং অন্যান্য কনফিগারেশন এনভায়রনমেন্ট ভ্যারিয়েবল থেকে লোড হবে
BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    # টেলিগ্রাম থেকে আসা আপডেট এখানে হ্যান্ডেল করা হবে
    update = request.get_json()
    if update:
        # আপনার বটের লজিক বা হ্যান্ডলার এখানে কল করতে হবে
        pass
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run()
