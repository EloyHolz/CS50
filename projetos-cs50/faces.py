EMOJI_DICT = {
    ":)": "🙂",
    ":(": "🙁",
    "Crying": "😭",
    "laughing": "😂"
}


def emoji_conv():
    print("Welcome to the Convertron 3000 - your favorite 'text to emoji' converter")
    mood = input("Write your mood today: ").lower().split(" ")
      
    emoji_result = [EMOJI_DICT.get(word, word) for word in mood]
    result_string = ' '.join(emoji_result)

    print("Your mood in emoji: ", result_string)

emoji_conv()
