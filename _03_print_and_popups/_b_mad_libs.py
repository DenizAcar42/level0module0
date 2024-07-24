from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Put this sentence in a pop-up message box:
    # "If you find yourself having to cross a piranha-infested river, here's how to do it..."
    verb = simpledialog.askstring(title = 'Mad_Libs', prompt="If you happen to come across a pack of homosexuals you... enter a verb")
    # Get the player to enter an adjective
    a = simpledialog.askstring(title= "Mad_Libs", prompt="enter an adjective")
    # Get the player to enter a type of liquid
    b = simpledialog.askstring(title= "Mad_Libs", prompt="enter an lquid")
    # Get the player to enter a body part
    c = simpledialog.askstring(title= "Mad_Libs", prompt="enter an body part")
    # Get the player to enter a verb
    d = simpledialog.askstring(title= "Mad_Libs", prompt="enter an verb")
    # Get the player to enter a place
    e = simpledialog.askstring(title= "Mad_Libs", prompt="enter an place")
    # The story below has has been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        "Gay people are more " + a + " during June, so make sure not to start a fight with them\n"
        ". Gay people are scared of " + b + " and will most\n"
        "likely act zesty as a form a defense to swat away the stright people and use their" + c + " to try to beat you up in a  " + verb + " fashion. Now \n"
        "if you can hide in the " + e + ", you might be able to get away from the homosexuals. Good luck and stay safe!"
    )
    messagebox.showinfo(title="story", message=story)
    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up

    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.

    # Run the window's .mainloop() method

