import json
from random import randint
from plyer import notification
from time import sleep
# Time span from user
time_span = int(input("Enter the time span for next notification[In minutes]: "))

time_out = 15
# Load English Dictionary in data
data = json.load(open("dictionary.json"))

# Gets all words in a list [All keys]
words = list(data.keys())

# Get length of words to generate random index
words_len = len(words)


# This Functions generates windows notification.
def show_notification(word, meaning):
    notification.notify(
        title="Word: " + word.capitalize(),
        message="Meaning: " + meaning,
        app_icon="dictionary.ico",
        timeout=time_out,
    )


# until user closes the program.
while True:
    random_word = words[randint(0, words_len)]
    word_meaning = data[random_word]
    show_notification(random_word, word_meaning)
    sleep(time_span * 60)