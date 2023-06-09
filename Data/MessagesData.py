import random


#Different types of hello messages possible
Hello_messages = ["hello","hola","hi","hey","hey yo","hey there","howdy","yo","bonjour","ciao","namaste"]

#Different types of hello messages replies
Hello_messages_Replies = [
    "Hello there!",
    "Hi, how's it going?",
    "Hey, what's up?",
    "Hey yo, what's happening?",
    "hey Yo",
    "Hey there, nice to see you!",
    "Howdy, partner!",
    "Yo, what's the word?",
    "Namaste, how are you doing?",
    "Greetings, how can I assist you today?",
    "Hello, it's a pleasure to meet you!",
    "Hey, how's your day treating you?",
    "Hi there, what brings you here?",
    "Hey, long time no see! What have you been up to?",
    "Hello, hope you're having a fantastic day!",
    "Hi, nice to see you again. What's new?",
    "Hey, how's life treating you lately?",
    "Greetings, ready for an amazing conversation?",
    "Hello, what can I do for you today?",
    "Hi there, how's everything going on your end?",
    "Hey, it's good to have you here. What's on your mind?",
    "Hello, hope you're enjoying your day so far!",
    "Hi, ready to dive into some interesting topics?",
    "Hey, what's the latest gossip? Fill me in!",
    "Greetings, how may I be of service to you?",
    "Hello, looking forward to our chat!",
    "Hi there, anything exciting happening in your life?",
    "Hey, let's catch up! What have you been doing lately?",
    "Hello, hope you're ready for a great conversation!",
    "Hi, what's the good word for today?",
    "Hey, how's the weather in your neck of the woods?",
    "Greetings, how's life treating you these days?",
    "Hello, it's a pleasure to connect with you!",
    "Hi there, what's the scoop on your end?",
    "Hey, what's cooking? Anything interesting happening?",
    "Hello, hope you're having a splendid day!",
    "Hi, nice to see you! How have you been?",
    "Hey, long time no chat! What have you been up to?",
    "Greetings, how can I make your day better?",
    "Hello, ready to dive into some intriguing conversations?",
    "Hi there, what's the latest?",
    "Hey, how's it hanging? Any exciting news?",
    "Hello, hope you're feeling awesome today!",
    "Hi, what's happening in your world?",
    "Hey, long time, no talk! What's new with you?",
    "Greetings, ready for some interesting discussions?",
    "Hello, how's your day shaping up?",
    "Hi there, anything interesting on your agenda?",
    "Hey, let's have a chat! What's on your mind?",
    "Hello, hope you're having a wonderful time!",
    "Hi, ready to explore new ideas and thoughts?",
    "Hey, what's the buzz? Share the latest!",
    "Greetings, how can I assist you today?",
    "Hello, it's nice to see you again!",
    "Hi there, how have you been lately?",
    "Hey, how's life treating you these days?",
    "Hello, ready for an engaging conversation?",
    "Hi, what brings you here today?",
    "Hey, long time no see! What's been happening?",
    "Greetings, hope you're having a fantastic day!",
    "Hello, nice to have you back. What's up?",
    "Hi there, any exciting news to share?",
    "Hey, how's your day going so far?",
    "Hello, hope you're ready for an interesting discussion!",
    "Hi, what's the latest scoop on your end?",
    "Hey, any exciting plans for the day?",
    "Greetings, how may I be of help to you?",
    "Hello, looking forward to our conversation!",
    "Hi there, what's new in your world?",
    "Hey, let's catch up! How have you been?",
    "Hello, hope you're having a great day!",
    "Hi, ready to dive into some fascinating topics?",
    "Hey, what's the talk of the town? Fill me in!",
    "Greetings, how can I assist you today?",
    "Hello, it's a pleasure to meet you!",
    "Hi there, how's your day going?",
    "Hey, what's going on in your life?",
    "Hello, hope you're having a wonderful day!",
    "Hi, nice to see you again. What's new?",
    "Hey, how's everything going with you?",
    "Greetings, ready for an interesting conversation?",
    "Hello, how can I help you today?",
    "Hi there, what's on your mind?",
    "Hey, any exciting plans for the day?",
    "Hello, hope you're ready for an engaging discussion!",
    "Hi, what's the latest news on your end?",
    "Hey, how's your day shaping up?",
    "Greetings, how's life treating you today?",
    "Hello, it's a pleasure to reconnect with you!",
    "Hi there, what's happening in your world?",
    "Hey, any interesting stories to share?",
    "Hello, hope you're having a fantastic time!",
    "Hi, nice to see you! How have you been?",
    "Hey, long time no chat! What's been going on?",
    "Greetings, how can I brighten your day?",
    "Hello, ready for some thought-provoking conversations?",
    "Hi there, what's the latest update?",
    "Hey, how's it going? Anything new?",
    "Hello, hope you're feeling great today!",
    "Hi, what's the buzz? Tell me everything!",
    "Hey, long time no talk! How have you been?",
    "Greetings, ready for an exciting chat?",
    "Hello, how's your day treating you?",
    "Hi there, anything interesting happening?",
    "Hey, let's have a conversation! What's on your mind?",
    "Hello, hope you're enjoying your day so far!",
    "Hi, ready to explore new ideas?",
    "Hey, what's the latest gossip? Fill me in!",
    "Greetings, how may I be of assistance to you?",
    "Hola",  # Spanish
    "Salutations",  # English
    "Greetings",  # English
    "Bonjour",  # French
    "Ciao",  # Italian
    "Namaste",  # Hindi
    "Konnichiwa",  # Japanese
    "Annyeonghaseyo",  # Korean
    "Hallo",  # German
    "Olá",  # Portuguese
    "Salaam",  # Arabic
    "Nǐ hǎo",  # Mandarin Chinese
    "Hej",  # Swedish
    "Merhaba",  # Turkish
    "Shalom",  # Hebrew
    "Privet",  # Russian
    "Sawasdee",  # Thai
    "Guten Tag",  # German
    "Dia duit",  # Irish
    "Hei",  # Norwegian
    "Szia",  # Hungarian
    "Dobrý den",  # Czech
    "Zdravo",  # Serbian
    "Aloha",  # Hawaiian
    "Sveiki",  # Latvian
    "Marhaba",  # Arabic
    "God dag",  # Danish
    "Kia ora",  # Maori
    "Kaixo",  # Basque
    "Ahoj",  # Slovak
    "Moïen",  # Luxembourgish
    "Labas",  # Lithuanian
    "Dzień dobry",  # Polish
    "Xin chào",  # Vietnamese
    "Halo",  # Indonesian
    "Sain baina uu",  # Mongolian
    "Mingalarba",  # Burmese
    "Zdravo",  # Bosnian
    "Salam",  # Persian
    "Përshëndetje",  # Albanian
    "Szia",  # Finnish
    "Salam",  # Urdu
    "Jambo",  # Swahili
    "Hallo",  # Dutch
    "Dobar dan",  # Croatian
    "Salut",  # Romanian
    "Moikka",  # Finnish
    "Hoi",  # Dutch
    "Tere",  # Estonian
    "Salut",  # Haitian Creole
    "Privyet",  # Ukrainian
    "Salam",  # Azerbaijani
    "Kumusta",  # Filipino
    "Sawubona",  # Zulu
]

def HelloReply():
    Index = random.randint(0, len(Hello_messages_Replies)-1)
    return Hello_messages_Replies[Index]
