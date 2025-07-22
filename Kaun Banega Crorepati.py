questions= [
    ["1. Who developed Python Programming Language?"
,"a) Wick van Rossum","b) Rasmus Lerdorf"," c) Guido van Rossumd", "d)Niene Stom",3],
    ["2. Which type of Programming does Python support?"
,"a) object-oriented programming","b) structured programming","c) functional programming","d) all of the mentioned",4],
     ["3. Which keyword is used for function in Python language?"
,"a) Function","b) def","c) Fun","d) Define",2],
    ["4. Which of the following character is used to give single-line comments in Python?"
,"a) //","b) #","c) !","d) /*",2],
    ["5. Python supports the creation of anonymous functions at runtime, using a construct called"
,"a) pi","b) anonymous","c) lambda","d) none of the mentioned",3],
    ["6. What does pip stand for python?"
,"a) Pip Installs Python","b) Pip Installs Packages","c) Preferred Installer Program","d) All of the mentioned",3],
    ["7. Which of the following is the truncation division operator in Python?"
,"a) |","b) //","c) /","d) % ",2],
    ["8. Which of the following functions is a built-in function in python?"
,"a) factorial()","b) print()","c) seed()","d) sqrt()",2],
     ["9. Which of the following is not a core data type in Python programming?"
,"a) Tuples","b) Lists","c) Class","d) Dictionary",3],
     ["10. Which one of the following is not a keyword in Python language?"
,"a) pass","b) eval","c) assert","d) nonlocal",2],

]

levels =[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0
for i in range(0, len(questions)):
       
    question = questions[i]
    if(question == questions[5]):
        ques=input("Would you like to continue the game or not (y/n):")
        if(ques =='y'):
            continue
        else:
            print("Thank you for participating, Better Luck Next Time")
            break
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f" {question[1]}          {question[2]} ")
    print(f" {question[3]}          {question[4]} ")
    reply = int(input("Enter your answer (1-4)  or  0 to quit:\n"))
    if (reply == 0):
       money = levels[i-1]
       break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs {levels[i]}")
        if(i == 4):
              money = 10000
        elif(i == 9):
            money = 320000   
    else:
        print("Wrong answer!!!") 
        break   

   
print(f"The money which you can take away is {money}")
print("hello")