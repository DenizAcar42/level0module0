from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer = simpledialog.askstring(title="Quiz_Game", prompt="Is the dress black and blue or white and gold?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer.lower() == "yes":
    #      // 4.  if the user's answer was correct, add one to their score 
        score = score+1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    elif answer.lower() == "no":
        score = score-1
    else:
        messagebox.showinfo("Invalid Input. Please write -yes- or -no-")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function
    messagebox.showinfo("Your score was: " + score.__str__() + " out of 1")
    
    # Run the window's .mainloop() method
    window.mainloop()
