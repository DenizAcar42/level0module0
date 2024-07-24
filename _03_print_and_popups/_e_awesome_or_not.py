from tkinter import messagebox, simpledialog, Tk
import random


def main():
    # Make a new window variable
    window = Tk()

    # Hide the window using the window's .withdraw() method
    window.withdraw()

    # 1. Make a variable equal to a positive number less than 4 using random.randint(0, 3)
    random_number = random.randint(0, 3)

    # 2. Print your variable to the console
    print(random_number)

    # 3. Get the user to enter something that they think is awesome
    user_input = simpledialog.askstring("Input", "Enter something awesome:")

    # 4. If your variable is 0
    if random_number == 0:
        messagebox.showinfo("Feedback", f"{user_input} is good ig")

    # 5. If your variable is 1
    elif random_number == 1:
        messagebox.showinfo("Feedback", f"{user_input} is kinda mid")

    # 6. If your variable is 2
    elif random_number == 2:
        messagebox.showinfo("Feedback", f"{user_input} is the worst")

    # 7. If your variable is 3
    elif random_number == 3:
        messagebox.showinfo("Feedback", "kys")

    # Run the window's .mainloop() method
    window.mainloop()


if __name__ == "__main__":
    main()
