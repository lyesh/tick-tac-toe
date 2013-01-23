import tkinter as tk

class Board():

    def finish_up(self):
        self.frame.quit()

    def draw_board(self):
        self.canvas = tk.Canvas(self.frame,width="13c",height="13c")
        self.canvas.create_rectangle("0.5c","0.5c","12.5c","12.5c")
        self.canvas.create_line("4.5c","0.5c","4.5c","12.5c")
        self.canvas.create_line("9c","0.5c","9c","12.5c")
        self.canvas.create_line("0.5c","4.5c","12.5c","4.5c")
        self.canvas.create_line("0.5c","9c","12.5c","9c")
        
        self.draw_o(0,0)
        self.draw_x(4,0)
        
        self.canvas.grid()
    
    def draw_x(self,x,y):
        x1 = str(x+1)+"c"
        x2 = str(x+3)+"c"
        y1 = str(y+1)+"c"
        y2 = str(y+3)+"c"        
        self.canvas.create_line(x1,y1,x2,y2)
        self.canvas.create_line(x2,y1,x1,y2)

    def draw_o(self,x,y):
        'draw an o at location (x,y). dimensions in cm'
        x1 = str(x+1)+"c"
        x2 = str(x+3)+"c"
        y1 = str(y+1)+"c"
        y2 = str(y+3)+"c"
        self.canvas.create_oval(x1,y1,x2,y2)
    
    def __init__(self):
        self.frame = tk.Frame()
        self.frame.grid()
        self.draw_board()

        quitButton = tk.Button(self.frame,\
                               text="Quit",\
                               command=self.finish_up)
        quitButton.grid()
        
        self.frame.mainloop(0)


