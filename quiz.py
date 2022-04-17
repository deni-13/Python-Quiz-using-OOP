#quiz app----

print("""********************************************
      
      
      welcome  To The Quiz!
      ********************************************""")
class Question():
    def __init__(self,que,ans):
        self.que=que
        self.ans=ans
q_list=[
"1+2 =?\na)3 \nb)4 \nc)6 \nd)19",
"Where is the capital of USA? \na)California \nb)Washington \nc)Berlin \nd)New York",
"What color is the apple =?\na)green \nb)orange \nc)black \nd)brown"
]

keys= [


Question(q_list[0],"a"),
Question(q_list[1],"b"),
Question(q_list[2],"a"),
]


def quizApp(keys):
    point=0
    for que in keys:
        ans=input(que.que + "\nPlease mark true one?")
        if ans==que.ans:
            point+=1
    print("Your points:  " + str(point)+ "/" + str(len(keys)))

quizApp(keys)
