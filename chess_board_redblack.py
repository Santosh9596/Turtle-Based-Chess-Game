

#turtle based chess board

from turtle import *

class chessBoard:
    speed(1000)

    
    print("CREATING CHESS BOARD...........")

def chess_Board():
    def draw_square():
        pendown()
        for i in range(4):
            forward(80)
            lt(90)
        forward(80)

        
    for i in range(8):

        penup()
        setpos(-330,-350+80*i)

        for j in range(8):

            
            if (i+j)%2 == 0:
                fillcolor('red')
                begin_fill()
                draw_square()
                end_fill()

                
            else:
                fillcolor('black')
                begin_fill()
                draw_square()
                end_fill()

                

    print("CHESS BOARD CREATED !!!!!")

    
chess_Board()
