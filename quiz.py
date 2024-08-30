from tkinter import *
import random
import tkinter.messagebox as tmsg

root = Tk()

class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option
        self.submit_button = None  # Initialize submit button attribute

    def ask_question(self):
        x= Label(text="\n\n\n\n\n\n\n\n\n")
        x.pack()
        self.label_prompt = Label(root, text=self.prompt, padx=4, pady=2, font="Arial 16 bold", relief=SUNKEN)
        self.label_prompt.pack(anchor="w")
        self.var = IntVar()
        self.var.set(0)
        option_labels = self.options
        self.radio1 = Radiobutton(root, text=f"1. {option_labels[0]}", variable=self.var, value=1, font="Arial 12 bold")
        self.radio1.pack(anchor="w")
        x1 = Label(text="\n")
        x1.pack()
        self.radio2 = Radiobutton(root, text=f"2. {option_labels[1]}", variable=self.var, value=2, font="Arial 12 bold")
        self.radio2.pack(anchor="w")
        x2 = Label(text="\n")
        x2.pack()
        self.radio3 = Radiobutton(root, text=f"3. {option_labels[2]}", variable=self.var, value=3, font="Arial 12 bold")
        self.radio3.pack(anchor="w")
        x3 = Label(text="\n")
        x3.pack()
        x.destroy()
        x1.destroy()
        x2.destroy()
        x3.destroy()

    def submit(self):
        return self.var.get()

    def check_answer(self, user_answer):
        return user_answer == self.correct_option

    def clear_question(self):
        self.label_prompt.destroy()
        self.radio1.destroy()
        self.radio2.destroy()
        self.radio3.destroy()
        if self.submit_button:
            self.submit_button.destroy()  # Destroy the submit button if it exists

def conduct_exam_for_subject(subject, questions):
    score = 0
    print(f"Starting {subject} exam...")
    for question in questions:
        question.ask_question()
        root.wait_variable(question.var)
        if question.check_answer(question.submit()):
            score += 1
        question.clear_question()
    print(f"{subject} Score: {score}")
    return score
def main():
    # Destroy the start button after it is clicked
    
    bl1.destroy()
    bl2.destroy()
    b1.destroy()
    n1.destroy()
    n2.destroy()
    n3.destroy()
    f1.destroy()
    # Destroy the n4 label
    n4.destroy()
    blS1 = Label(text="\n\n")
    blS1.pack()
    s1 = Label(root, text="SECTION : PHYSICS", fg="black",bg="orange", font="Arial 19 bold" , relief=SUNKEN)
    s1.pack()
    # Physics questions
    questions_list_p = [
        Question("\nWhat is the unit of stress?", ["N/m²", "K/m", "Nm"], 1),
        Question("\nWhat is the upward force experienced by a body, when it is immersed in a fluid, known as?", ["tangential force", "gravitational force", "Buoyant force"], 3),
        Question("\nWhat happens to a body when its density is greater than the density of the fluid?", ["It flows", "It sinks", "None of this"], 2),
        Question("\nWhy is a small liquid drop in spherical shape?", ["Surface tension", "low viscosity", "low density"], 1)]
    random.shuffle(questions_list_p)
    score_p = conduct_exam_for_subject("Physics", questions_list_p)
    s1.destroy()
    blS1.destroy()
    
    blS2 = Label(text="\n\n")
    blS2.pack()
    s2=Label(root,text="SECTION : CHEMISRY",bg="yellow" ,fg="black",font="Arial 19 bold",relief=SUNKEN)
    s2.pack()
    
    # Chemistry questions
    questions_list_c = [
        Question("\nWhich among the following methods can be used to remove the permanent hardness in water due to calcium or magnesium sulphates?", ["Sulphonate method", "Nitrate method ", "Zeolite method "], 3),
        Question("\nBleaching Powder is a compound of _______?", ["Calcium ", "Sodium ", "Magnesium "],1 ),
        Question("\nWhat happens to the weight of Iron, when it rusts?", ["Increases for long time ", " Decreases then increases ", "Increases then decreases "],3 ),
        Question("\nWhich among the following is an example of a Chemical Change?", ["Rusting of iron ", "Magnetisation of iron ", "Melting of iron "],1 )]
    random.shuffle(questions_list_c)
    score_c = conduct_exam_for_subject("Chemistry", questions_list_c)
    s2.destroy()
    blS2.destroy()
    
    blS3 = Label(text="\n\n")
    blS3.pack()
    s3=Label(root,text="SECTION : BIOLOGY",bg="green" ,fg="black",font="Arial 19 bold",relief=SUNKEN)
    s3.pack()
    # Biology questions
    questions_list_b = [
        Question("\nWhich part of the Human Body stores Glycogen?", ["Liver ", "Intestine ", " Pancreas "],1 ),
        Question("\n Cirrhosis is a disease that affects which among the following organs?", ["Kidney ", "Liver ", "Pancreas "],2),
        Question("\nWhen the body’s immune system cells destroy the insulin producing beta cells of the pancreas is termed as ________?", ["Type 1 diabetes ", "Type 2 diabetes ", "hybrid diabetes"],1 ),
        Question("\nWhich among the following function as locus of biochemical reactions? ", ["Cell plasma", "Cell membrane ", "Cell walls "],2 )]
    random.shuffle(questions_list_b)
    score_b = conduct_exam_for_subject("Biology", questions_list_b)
    s3.destroy()
    blS3.destroy()
    question_list_t=questions_list_b+questions_list_c+questions_list_p
    size=len(question_list_t)
    score_t=score_p+score_b+score_c
    blS4 = Label(text="\n\n\n\n\n\n\n\n")
    blS4.pack()
    f2 = Frame(root, bg="grey", borderwidth=2)
    f2.pack()
    if score_t<size/2:
        
        r=Label(f2,text="Result : Not good \nYour score in Physics",fg="red",bg="grey",font="Arial 19 bold",pady=8,padx=4)
        r.pack()
        rp=Label(f2,text=f"Your score in Physics: {score_p}",bg="grey",font="Arial 12",padx=2,pady=4)
        rp.pack()
        rc=Label(f2,text=f"Your score in Chemistry: {score_c}",bg="grey",font="Arial 12",padx=2,pady=4)
        rc.pack()
        rb=Label(f2,text=f"Your score in Biology: {score_b}",bg="grey",font="Arial 12",padx=2,pady=4)
        rb.pack()
    else:
        r=Label(f2,text="Result : Great Job \nYour score in Physics",fg="green",bg="grey",font="Arial 19 bold",pady=8,padx=4)
        r.pack()
        rp=Label(f2,text=f"Your score in Physics: {score_p}",bg="grey",font="Arial 112",padx=2,pady=4)
        rp.pack()
        rc=Label(f2,text=f"Your score in Chemistry: {score_c}",bg="grey",font="Arial 12",padx=2,pady=4)
        rc.pack()
        rb=Label(f2,text=f"Your score in Biology: {score_b}",bg="grey",font="Arial 12",padx=2,pady=4)
        rb.pack()

    print(f"Physics Score: {score_p}")
    print(f"Chemistry Score: {score_c}")
    print(f"Biology Score: {score_b}")

root.geometry('400x400')
root.minsize(200, 100)
n3 = Label(text="WELCOME TO EXAM SIMULATOR", fg="Black", font="Arial 16 bold", relief=SUNKEN, justify="left")
n3.pack(anchor="n")
bl1 = Label(text="\n\n")
bl1.pack()
f1 = Frame(root, bg="black", borderwidth=2)
f1.pack()
n1 = Label(f1, text="Rules & Instruction For Exam", fg="Red", font="Arial 13 bold")
n1.pack()
n2 = Label(text="\n1. You can enter answer only one time\n2. You can choose only given option.\n3.If your answer is correct then you get 4 marks.\n4.No negetive marking", font="Arial 11 bold", fg="Red")
n2.pack(anchor="center")
bl2 = Label(text="\n\n")
bl2.pack()
n4 = Label(text="Are you ready for the exam?", font="Arial 11 bold", fg="black", relief=SUNKEN)
n4.pack(anchor='w')
b1 = Button(root, text="START", bg="green", fg="white", command=main)
b1.pack(anchor="w")
root.mainloop()

