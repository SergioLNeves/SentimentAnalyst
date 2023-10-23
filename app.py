from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    termo = request.form.get('termo')
    with open('../TesteIA/texto/termo.txt', 'w') as arquivo:
            arquivo.write(termo)
    return render_template('ResultadoBusca.html', termo=termo)


if __name__ == '__main__':
    app.run(debug=True)
