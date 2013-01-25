import board
import game


def canvas_callback(event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    print(x,y)
    
def place_piece():
    pass

game = game.Game()
board = board.Board()

board.canvas.tag_bind()

board.frame.mainloop(0)