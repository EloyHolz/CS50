def emoji_conv():
    print("Welcome to the Convertron 3000 -your favorate text to emoji convertor")
    mood = input("Write your mood today: ").split(" ")
    
    
    dict = {
        "happy":"🙂",
        "sad": "🙁",
        "feliz": "🙂",
        "triste":"🙁",
        ":)":"🙂",
        ":(":"🙁",
        "Crying":"😭",
        "laughing":"😂"
    }  



    print(dict.get(mood))     

emoji_conv()