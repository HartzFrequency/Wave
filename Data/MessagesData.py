import random


#Different types of hello messages possible
Hello_messages = ["hello","hola","hi","hey","hey yo","hey there","howdy","yo","bonjour","ciao","namaste"]

#Different types of hello messages replies
Hello_messages_Replies = ["Hello there!","Hi, how's it going?","Hey, what's up?","Hey yo, what's happening?","hey Yo","Hey there, nice to see you!","Howdy, partner!","Yo, what's the word?","Namaste, how are you doing?"]

def HelloReply():
    Index = random.randint(0, len(Hello_messages_Replies)-1)
    return Hello_messages_Replies[Index]