import json

log_file = "chat_history.jsonl"
def log_json(entry):
    with open(log_file, "a", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")