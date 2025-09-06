import time as t #importing as t just makes it easier as i can wrtite t.start rather than time.start
import random

#make question
def create_q(max_num,numofquestion):
    while True:
        operations= ("+","-")#write as string and use eval() later
        a=random.randint(1,max_num)
        b=random.randint(1,max_num)
        op=random.choice(operations)
    #store the question in a variable
        result =(f"{a}{op}{b} ")
        return result #no brackets as im not calling a function

def ask_q(max_num,numofquestion):
    print("Current score: 0")
    score=0 
    i=0#new variable to control the number of displayed questions
    total_time = 0 #So it can be used in case of value error
    correct=0
    while i<numofquestion:
        try:
            start_time = t.time()#start countiung time
            question=create_q(max_num//2, numofquestion)
            correct_ans = eval(question) #eval evaluates the operation intially counted as string
            user_ans = int(input(question))
            end_time= t.time()#end counting time
            elapsed_time = int(end_time - start_time)#calculate elapsed time
            total_time+=elapsed_time
            
            if user_ans == correct_ans:
                correct+=1
                i+= 1                                             
                point = int(10-elapsed_time)
                score+= point
                print(f"Correct answer! You took {round(elapsed_time,3)} seconds, Points awarded : {point}")
                 
            else:
                i+= 1              
                print(f"Incorrect! No points awarded ")                
        
        except ValueError:
            end_time= t.time()
            elapsed_time = int(end_time - start_time)
            total_time+=elapsed_time
            i+=1
            print("Enter a number!! No points awarded")
        average_time = (elapsed_time/numofquestion)
    
        try:
            print("""Final boss!!!!
Challenge question!: Correct answer grants 20 points!!!""")
            start_time = t.time()#start countiung time
            challenge_question=create_q(max_num*2)
            correct_ans = eval(challenge_question) #eval evaluates the operation intially counted as string
            user_ans = int(input(challenge_question))
            end_time= t.time()#end counting time
            elapsed_time = int(end_time - start_time)#calculate elapsed time
            total_time+=elapsed_time
            
            if user_ans == correct_ans:
                correct+=1
                i+= 1                                             
                point = int(10-elapsed_time)
                score+= point
                print(f"Correct answer! You took {round(elapsed_time,3)} seconds, Points awarded : {point}")
                 
            else:
                i+= 1              
                print(f"Incorrect! No points awarded ")
            
    print(f"""Quiz over! 
Your total score was:  {score}
You answered {(correct/numofquestion)*100}% of the questions correctly
You average response time was: {average_time}s""")#only print after i=numofquestions(Multiline strings are very cool)

print("--------------------------------------Welcome to the (not so) ULTIMATE math quiz--------------------------------------")


#Set difficulty parameters for chosen difficulty
while True:
    choice = input("""Choose your difficulty: 
1)Easy 
2)Medium 
3)Hard 
-->""").lower()
    try:
        if choice == "1":
            ask_q(10,4)
            break
        elif choice == "2":    
            ask_q(20,9)
            break
        elif choice == "3":
            ask_q(50,14)
            break
    except ValueError:
        ("Choose a Valid difficulty ")
        
