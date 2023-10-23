from transformers import pipeline

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

with open('../TesteIA/texto/termo.txt', 'r') as arquivo:
  sentences = arquivo.read().splitlines()
# sentences = ["I am not having a great day"]

model_outputs = classifier(sentences)
first_emotion_position = model_outputs[0][0]['label']
print(first_emotion_position)