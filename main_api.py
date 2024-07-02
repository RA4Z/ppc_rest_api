from flask import Flask, request, jsonify
from flask_cors import CORS
import rest_functions

app = Flask(__name__)
CORS(app)

@app.route('/gemini', methods=['POST'])
def process_message():
    return rest_functions.process_message_function(request)


@app.route('/quit', methods=['POST'])
def quit_system():
    return rest_functions.quit_system_function(request)


@app.route('/search', methods=['POST'])
def search_file():
    return rest_functions.search_file_function(request)


@app.route('/secretary', methods=['POST'])
def search_secretary_procedure():
    return rest_functions.search_secretary_procedure_function(request)


@app.route('/WenIndicators/Indicators/Display')
def get_wen_indicators():
    return jsonify(rest_functions.get_json_file("indicators/data/indicadores.json"))


@app.route('/WenIndicators/Database/Display')
def get_wen_database():
    return jsonify(rest_functions.get_json_file("indicators/rest/wen_indicators_database.json"))


@app.route('/WenIndicators/Replace/Display')
def get_wen_replace():
    return jsonify(rest_functions.get_json_file("indicators/replace_list.json"))


@app.route('/WenIndicators/Results/Display')
def get_wen_results():
    return jsonify(rest_functions.get_json_file("indicators/rest/wen_indicators_results.json"))


@app.route('/update')
def update_api():
    return rest_functions.update()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
