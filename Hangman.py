import random
import hangman_stages

word=[
    "apple", "banana", "grape", "orange", "melon", "cherry", "peach", "lemon", "plum", "berry",
    "car", "train", "plane", "truck", "bike", "scooter", "bus", "van", "jeep", "subway",
    "book", "pen", "pencil", "paper", "notebook", "eraser", "marker", "ruler", "stapler", "sharpener",
    "table", "chair", "couch", "desk", "shelf", "bed", "lamp", "mirror", "sofa", "door",
    "dog", "cat", "rabbit", "horse", "cow", "sheep", "goat", "pig", "duck", "chicken",
    "sun", "moon", "star", "sky", "cloud", "rain", "snow", "wind", "storm", "fog",
    "water", "juice", "milk", "coffee", "tea", "soda", "beer", "wine", "oil", "soup",
    "shirt", "pants", "dress", "shoes", "socks", "hat", "scarf", "gloves", "jacket", "coat",
    "phone", "laptop", "tablet", "camera", "tv", "remote", "charger", "speaker", "mouse", "keyboard",
    "door", "window", "floor", "wall", "roof", "ceiling", "curtain", "mat", "lock", "key",
    "river", "lake", "ocean", "beach", "mountain", "valley", "forest", "desert", "hill", "island",
    "game", "play", "win", "lose", "score", "team", "goal", "match", "race", "kick",
    "school", "class", "student", "teacher", "lesson", "exam", "test", "homework", "subject", "grade",
    "music", "song", "dance", "band", "singer", "guitar", "drum", "piano", "violin", "flute",
    "movie", "film", "actor", "scene", "script", "camera", "director", "studio", "ticket", "screen",
    "job", "work", "office", "boss", "salary", "career", "meeting", "task", "resume", "interview",
    "city", "village", "town", "street", "road", "bridge", "park", "building", "hotel", "house",
    "food", "bread", "rice", "meat", "fish", "egg", "cake", "fruit", "vegetable", "sugar",
    "family", "father", "mother", "brother", "sister", "uncle", "aunt", "cousin", "baby", "child",
    "happy", "sad", "angry", "excited", "tired", "scared", "bored", "proud", "jealous", "surprised",
    "clean", "dirty", "fast", "slow", "hot", "cold", "wet", "dry", "new", "old",
    "big", "small", "long", "short", "high", "low", "strong", "weak", "hard", "soft",
    "red", "blue", "green", "yellow", "black", "white", "purple", "brown", "pink", "orange",
    "yes", "no", "maybe", "please", "sorry", "thank", "hello", "goodbye", "hi", "bye",
    "clock", "watch", "alarm", "time", "minute", "hour", "second", "day", "night", "week",
    "face", "head", "hand", "arm", "leg", "foot", "eye", "ear", "nose", "mouth",
    "king", "queen", "prince", "princess", "castle", "sword", "knight", "dragon", "crown", "shield",
    "tool", "hammer", "nail", "screw", "saw", "drill", "tape", "glue", "wire", "wrench",
    "money", "cash", "coin", "note", "bank", "card", "bill", "price", "shop", "sale"
]
array_word=random.choice(word)
lives=6
display=[]
for k in range(len(array_word)):
       display+='_'
print("Welcome to the Game!")
Finish=False

while not Finish and '_' in display:
        print(display)
        guessed_letter=input("Write the guessed word: ")
        
        for position in range(len(array_word)):

                if guessed_letter==array_word[position]:
                        display[position]=guessed_letter

        
                        
        if guessed_letter not in array_word:
                        lives-=1
                        print('Wrong Guess')
                        print('Lives=',lives)
                        print(hangman_stages.stages[lives])

        if lives==0:
                        print('You lose the game')
                        print('coorect word is:',array_word)
                        Finish=True
        
if lives>0:
        print('You won the game')