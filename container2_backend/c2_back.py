from flask import Flask, request, jsonify
import nlpcloud
import threading
from c2_font import launch_gui  # Replace `your_gui_file` with the filename (without .py)

app = Flask(__name__)

# Load the API key from environment variables
api_key = "14082413c377e94388813b49f39b9125545d98a8"

# Initialize the NLPCloud Clients
lang_detect_client = nlpcloud.Client("python-langdetect", api_key, gpu=False)
ner_client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=True)

@app.route("/nlp/language_detection", methods=["POST"])
def language_detection():
    data = request.get_json()
    paragraph = data.get("text")

    if not paragraph:
        return jsonify({"error": "Paragraph can't be empty"}), 400

    result = lang_detect_client.langdetection(paragraph)

    if "languages" not in result:
        return jsonify({"error": "Error in language detection"}), 500

    languages = result['languages']
    language_results = [{"language": list(lang.keys())[0], "score": list(lang.values())[0] * 100} for lang in languages]

    return jsonify({"languages": language_results}), 200

@app.route("/nlp/ner", methods=["POST"])
def named_entity_recognition():
    data = request.get_json()
    paragraph = data.get("text")
    search_entity = data.get("entity")

    if not paragraph:
        return jsonify({"error": "Paragraph can't be empty"}), 400
    if not search_entity:
        return jsonify({"error": "Entity can't be empty"}), 400

    result = ner_client.entities(paragraph, searched_entity=search_entity)

    if "entities" not in result:
        return jsonify({"error": "Error in named entity recognition"}), 500

    entities = [{"text": entity['text'], "start": entity['start'], "end": entity['end']} for entity in result['entities']]

    return jsonify({"entities": entities}), 200

@app.route("/start_gui", methods=["POST"])
def start_gui():
    try:
        threading.Thread(target=launch_gui).start()
        return jsonify({"message": "GUI launched successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to launch GUI: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
