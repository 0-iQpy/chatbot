import requests
import json
from datetime import datetime, timedelta, timezone
from chat_log import log_json

url = "http://localhost:11434/api/generate"
model = "llama3.2:1b"

# Define timezone UTC+8
tz_ph = timezone(timedelta(hours=8))

while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit"]:
        break

    user_entry = {
        "timestamp": datetime.now(tz_ph).isoformat(),
        "role": "user",
        "message": user
    }
    log_json(user_entry)

    payload = {"model": model, "prompt": user}
    response_text = ""

    with requests.post(url, data=json.dumps(payload), stream=True) as r:
        print("Bot:", end=" ", flush=True)
        for line in r.iter_lines():
            if line:
                data = line.decode("utf-8")
                if '"response"' in data:
                    token = data.split('"response":"')[1].split('"')[0]
                    print(token, end="", flush=True)
                    response_text += token
        print()

    bot_entry = {
        "timestamp": datetime.now(tz_ph).isoformat(),
        "role": "bot",
        "message": response_text
    }
    log_json(bot_entry)