from googletrans import Translator

def traduzir(texto):
    translator = Translator()
    traducao = translator.translate(texto, src='pt', dest='en')
    return traducao.text

with open('../SentimentAnalyst/texto/termo.txt', 'r') as arquivo:
  sentences = arquivo.read()

texto_para_traduzir = sentences
texto_traduzido = traduzir(texto_para_traduzir)
with open('../SentimentAnalyst/texto/termo_traduzido.txt', 'w') as arquivo:
  arquivo.write(texto_traduzido)