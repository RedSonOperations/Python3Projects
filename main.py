import re
import long_responses as long



def message_prob(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty=0
    has_required_words = True

    #counts how many words are present in each predefined message
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    #Calculates percent of recognized words in user message
    percentage = float(message_certainty)/float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_prob(message, list_of_words, single_response)

    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'yo', 'heyo'], single_response=True)
    response("I'm doing fine, and you?", ['how', 'ddd', 'dde', 'ddg', 'are', 'you', 'doing', 'up'], required_words=['doing'])
    response('Thank you!', ['nice', 'you', 'are', 'awesome', 'cool', 'innovative', 'have',
                            'fun', 'jjjj'], required_words=['cool', 'innovative'])
    response('I am SimpleBot!', ['who', 'are', 'you' 'what', "what's", 'is', 'your',
                                 'name'], required_words=['who'])
    response('I hope to see you soon!', ['bye', 'goodbye', 'farewell', 'later'], required_words=['bye', 'see'])
    response('I enjoy doing whatever you instruct me to do!', ['what', 'do', 'fun', 'favorite', 'like'], required_words=['enjoy'])
    response("You should search for that on Google!",
    ['what', 'how', 'many', 'in', 'are' 'to', 'do', 'have', 'is', 'in', 'i'], required_words=['many', 'how'])
    response(long.R_EATING, ['what', 'do', 'you', 'like', 'meal' 'eating', 'eat', 'ddd'], required_words=['eat'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(input):
    split_message=re.split(r'\s+|[,;?!.-]\s*', input.lower())
    response=check_all_messages(split_message)
    return response

#response system test
while True:
    print('Bot: ' + get_response((input('You: '))))


