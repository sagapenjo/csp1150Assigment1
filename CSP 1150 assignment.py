import time as t #importing as t just makes it easier as i can wrtite t.start rather than time.start
import random

print("--------------------------------------Welcome to the (not so) ULTIMATE math quiz--------------------------------------")
choice = input("""Choose your difficulty: 
1)Easy 
2)Medium 
3)Hard 
-->""").lower()

#Set difficulty parameters for chosen difficulty
while True:
    try:
        if choice == "1":
            ask_q(10,5)
            break
        elif choice == "2":    
            ask_q(20,10)
            break
        elif choice == "3":
            ask_q(50,15)
            break
    except ValueError:
        ("Choose a Valid difficulty ")

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
    while i<numofquestion:
        try:
            start_time = t.time()#start countiung time
            question=create_q(max_num, numofquestion)
            correct_ans = eval(question) #eval evaluates the operation intially counted as string
            user_ans = int(input(question))
            
            if user_ans == correct_ans:
                i+= 1
                score+= 10
                end_time= t.time()#end counting time
                elapsed_time = int(end_time - start_time)#calculate elapsed time
                actual_score= (score-elapsed_time)
                print(f"Correct answer! You took {round(elapsed_time,2)} seconds, Current score: {actual_score}")
                 
            else:
                i+= 1              
                print(f"Incorrect! No points awarded ")                
        
        except ValueError:
            i+=1
            print("Enter a number!! No points awarded")
    average_time = (elapsed_time/numofquestion)
    print(f"""Quiz over! 
Your total score was:  {score}
You average response time was: {average_time}s""")#only print after i=numofquestions(Multiline strings are very cool)


        
