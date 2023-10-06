import os
from fpdf import FPDF
import random

#Input target question bank directory
target_dir=r"C:\Users\denni\OneDrive\Desktop\Coding\Python\REE_Quiz_Maker\REE-Quiz-Maker\QuestionBank"

#List all the directories
subjects=os.listdir(target_dir)
print("\n",subjects, "\n")

#Pick a subject
while True:
    try:        
        subject_dir=int(input("Select a subject index: "))
        while subject_dir>(len(subjects)-1):
            subject_dir=int(input("Select a subject index: "))
        break
    except:
        print("Invalid index")

#Print current working directory
target_dir=os.path.join(target_dir, subjects[subject_dir])
print(f"\nThis is your working directory: {target_dir} \n")

print(os.listdir(target_dir),"\n")

#Create a dictionary that insert what subject top choose and how many questions to choose randomly
question_number=dict()
while True:
    subject= input("Enter desired subject or exit: ")
    if subject=="Exit" or subject=="exit":
        break
    elif subject not in os.listdir(target_dir):
        print("Please select a proper subject")
        continue
    else:
        total_questions= len(os.listdir(os.path.join(target_dir, subject)))
        print(f"Total Question in this bank: {total_questions}")
        while True: 
            try:
                num_questions=int(input("Enter number of questions: "))
                if num_questions>total_questions:
                    print("Number of questions exceeded the total question in the bank")
                    continue
                else:
                    question_number[subject]=num_questions
                    break
            except:
                print("Invalid Input")
                continue


print(question_number)

#Dictionary Created
picked_questions={}
for key, value in question_number.items():

    #List of all questions in a certain key
    list_questions=(os.listdir(os.path.join(target_dir, key)))
    list_questions.sort()
    for i in range(value):
        while True:
            random_index=random.randint(0,len(list_questions)-1)
            if random_index in picked_questions.values():
                continue
            else:
                picked_questions[key,i]=list_questions[random_index]
                break
print(picked_questions)

#Shuffle the picked index
random_items= list(picked_questions.items())
random.shuffle(random_items)
shuffled_picked_questions=dict(random_items)

#Create List for picked questions
for key,value in shuffled_picked_questions.items():
    print(key[0],value)
