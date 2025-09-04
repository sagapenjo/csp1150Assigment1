import time as t
import random

def create_q(maxnum, numofquestion):
    operations= ("+","-","*","/")
    a=random.randint(1,maxnum)
    b=random.randint(1,maxnum)
    op=random.choice(operations)
     
    