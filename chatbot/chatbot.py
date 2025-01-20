import re
import long_responses as long


#This will check all the messages
def message_probablity(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words=True
    
    for word in user_message:
        if word in recognised_words:
            message_certainty+=1
    
    
    #calculates percentage of recognised words
    percentage = float(message_certainty)/ float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
        
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    
def check_all_messages(message):
    highest_probablity_list = {}
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_probablity_list
        highest_probablity_list[bot_response] = message_probablity(message, list_of_words, single_response, required_words)
        
        
    #resonse-------------------------------------------------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
 
    best_match = max(highest_probablity_list, key=highest_probablity_list.get)
    print(highest_probablity_list)
    
    return best_match

#TAke user input
def get_response(user_input):
    split_message = re.split(r'\s+\[,;.!:?-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#testing response
while(True):
    print ('bot : ', get_response(input('you: ')))
