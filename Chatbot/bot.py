from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
from soundplayer import transsent


CORPUS_FILE = "chat.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        answer = str(chatbot.get_response(query))
        print(f"🪴 {answer}")
        transsent(answer)
