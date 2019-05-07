from chatbot import chatbot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Mr Robot")
conversation = [
    "Olá",
    "E ae",
    "Como vai você?",
    "Sou um robô, não tenho sentimentos, mas obrigado por perguntar ¯\_(ツ)_/¯",
    "Bom saber :)",
    "Valeu",
    "De nada."
]
trainer = ListTrainer(chatbot)
trainer.train(conversation)
response = chatbot.get_response("Dae")
print(response)


##

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

