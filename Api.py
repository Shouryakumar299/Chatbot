# api.py
import json

def convert_input_to_json(user_input: str):
    """Convert GUI input into JSON."""
    return {
        "message": user_input,
        "meta": {"source": "customtkinter"}
    }


def convert_output_from_json(model_output: str):
    """Convert model's JSON output to normal text."""
    try:
        data = json.loads(model_output)
        return data.get("response", "No 'response' found in JSON.")
    except json.JSONDecodeError:
        return "Invalid JSON returned from model."
