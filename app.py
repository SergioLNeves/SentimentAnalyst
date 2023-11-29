from flask import Flask, render_template, request
import subprocess


app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    termo = request.form.get('termo')
    with open('../SentimentAnalyst/texto/termo.txt', 'w') as arquivo:
            arquivo.write(termo)
    subprocess.run(["python", "TranslateIA.py"])
    subprocess.run(["python", "EmotionIA.py"])
    with open('../SentimentAnalyst/texto/termo_traduzido.txt', 'r') as arquivo:
        resposta = arquivo.read()
    return render_template('ResultadoBusca.html', termo=termo, resposta=resposta)


if __name__ == '__main__':
    app.run(debug=True)
