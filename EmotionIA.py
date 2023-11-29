from transformers import pipeline
import subprocess

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

with open('../SentimentAnalyst/texto/termo_traduzido.txt', 'r') as arquivo:
  sentences = arquivo.read().splitlines()

model_outputs = classifier(sentences)
first_emotion_position = model_outputs[0][0]['label']
with open('../SentimentAnalyst/texto/sentimento.txt', 'w') as arquivo:
  arquivo.write(first_emotion_position)