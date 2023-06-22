from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

bandas = [
    {"id": 1, "nombre": "Metallica", "Marca": "Gibson"},
    {"id": 2, "nombre": "Muse", "Marca": "Fender"},
    {"id": 3, "nombre": "Led Zeppelin", "Marca": "Epiphone"}
]

@app.route('/bandas', methods=['GET'])
def obtener_bandas():
    return jsonify(bandas)

@app.route('/bandas/<int:banda_id>', methods=['GET'])
def obtener_banda_por_id(banda_id):
    banda = next((p for p in bandas if p['id'] == banda_id), None)
    if banda:
        return jsonify(banda)
    return jsonify({'mensaje': 'Banda no encontrada'}), 404


@app.route('/', methods=['GET'])
def index():
    return render_template('bandas.html', bandas=bandas)

if __name__ == '__main__':
    app.run()
