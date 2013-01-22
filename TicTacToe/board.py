import tkinter as tk

class Board():
    frame = tk.Frame()
    frame.grid()

    def finish_up(self):
        self.frame.quit()
    
    def __init__(self):
        quitButton = tk.Button(self.frame,\
                               text="Quit",\
                               command=Board.finish_up)
        quitButton.grid()
        self.frame.mainloop(0)


