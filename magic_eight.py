import random
def ask_input():
    answer_list =["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.",
"You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.",
"Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.",
"Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.",
"Outlook not so good.","Very doubtful."] 
    
    question=input("What's your question?")
    while(question != "quit"):
        if question[-1] != '?':
            print("I'm sorry, I can only answer questions.")
        else:
            answer=answer_list[randrange(20)]
        question = input("What's your question?")


