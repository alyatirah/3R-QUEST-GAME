from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

players = []

items = [
    {"name": "Botol Plastik", "type": "plastik", "recyclable": True, "image": "botol_plastik.png"},
    {"name": "Kertas Surat", "type": "kertas", "recyclable": True, "image": "kertas_surat.png"},
    {"name": "Tin Aluminium", "type": "logam", "recyclable": True, "image": "tin_aluminium.png"},
    {"name": "Kotak Karton", "type": "kertas", "recyclable": True, "image": "kotak_karton.png"},
    {"name": "Botol Kaca", "type": "kaca", "recyclable": True, "image": "botol_kaca.png"},
    {"name": "Kotak Plastik", "type": "plastik", "recyclable": True, "image": "kotak_plastik.png"},
    {"name": "Kertas Majalah", "type": "kertas", "recyclable": True, "image": "kertas_majalah.png"},
    {"name": "Tin Minuman", "type": "logam", "recyclable": True, "image": "tin_minuman.png"},
    {"name": "Botol Sabun", "type": "plastik", "recyclable": True, "image": "botol_sabun.png"},
    {"name": "Kertas Nota", "type": "kertas", "recyclable": True, "image": "kertas_nota.png"},
]

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    player_name = data.get('player_name')
    score = data.get('score')
    mode = data.get('mode')
    players.append({"name": player_name, "score": score, "mode": mode})
    return jsonify({"player": player_name, "score": score})

if __name__ == '__main__':
    app.run(debug=True)

