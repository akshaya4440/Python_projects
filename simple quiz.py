print("Welcome to the Simple Quiz Game!🎉")
#dictionary- stores question as key and answer as value
questions={"What is the name of the largest ocean on Earth?":"Pacific Ocean","What is the capital of India?":"Delhi","Which planet is known as the Red Planet?":"Mars","What is the boiling point of water in Celsius?":"100","Which city is called the City of Winds?":"Chicago","Which organ in the human body is responsible for the secretion of bile?":"Liver","Which state is known as the Land of the Rising Sun?":"Arunachal Pradesh","What gas do plants need for photosynthesis?":"Carbon dioxide","Who developed Python Programming Language?":"Guido van Rossum","Who is the founder of Microsoft?":"Bill Gates"}
#initially score is set to zero.
score=0 #score starts fresh everytime
#keep running the quiz until the user wants to end
while True:
    for question,answer in questions.items(): #goes through every question-answer pair 
        user_answer=input (question) #displays each question and waits for user answer.
        #compares user answer with correct answer 
        if user_answer.strip().lower()==answer.lower(): #(case sensitive and removes extra spaces)
            print("✅Correct answer\n")#if answer is correct 
            score+=1 #increases score if correct 
        else:
            print(f"❌ Wrong!! Correct answer is {answer}\n")  #if answer is wrong

    print(f"Quiz completed! Your final score is {score}/{len(questions)}😊🎉")#shows total score after all questions
    
    #ask if user wants to play again 
    play_again=input ("Do you want to play again? (yes/no):").strip().lower()
    #break the loop if answer is not yes 
    if play_again!="yes":
        print("Thankyou for playing!🤝")
        break #ends the loop and finishes the program.
    