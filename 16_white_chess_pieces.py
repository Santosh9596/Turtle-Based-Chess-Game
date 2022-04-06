import chess_board_redblack
import os
from turtle import *
sc = Screen()

def chess_pieces():

    Rook = Turtle()
    Rook.penup()
    sc.register_shape('Rook.gif')
    Rook.shape('Rook.gif')
    Rook.setpos(-290,-310)



    Knight = Turtle()
    Knight.penup()
    sc.register_shape('Knight.gif')
    Knight.shape('Knight.gif')
    Knight.setpos(-210,-310)



    Bishop = Turtle()
    Bishop.penup()
    sc.register_shape('Bishop.gif')
    Bishop.shape('Bishop.gif')
    Bishop.setpos(-130,-310)



    King = Turtle()
    King.penup()
    sc.register_shape('King.gif')
    King.shape('King.gif')
    King.setpos(-50,-310)



    Queen = Turtle()
    Queen.penup()
    sc.register_shape('Queen.gif')
    Queen.shape('Queen.gif')
    Queen.setpos(30,-310)


    Bishop_R = Bishop.clone()
    Bishop_R.setpos(110,-310)

    Knight_R = Knight.clone()
    Knight_R.setpos(190,-310)

    Rook_R = Rook.clone()
    Rook_R.setpos(270,-310)

    Pawn_1 = Turtle()
    Pawn_1.penup()
    sc.register_shape('Pawn.gif')
    Pawn_1.shape('Pawn.gif')
    Pawn_1.setpos(-290,-230)

    Pawn_2 = Pawn_1.clone()
    Pawn_2.setpos(-210,-230)


    Pawn_3 = Pawn_1.clone()
    Pawn_3.setpos(-130,-230)



    Pawn_4 = Pawn_1.clone()
    Pawn_4.setpos(-50,-230)


    Pawn_5 = Pawn_1.clone()
    Pawn_5.setpos(30,-230)


    Pawn_6 = Pawn_1.clone()
    Pawn_6.setpos(110,-230)


    Pawn_7 = Pawn_1.clone()
    Pawn_7.setpos(190,-230)


    Pawn_8 = Pawn_1.clone()
    Pawn_8.setpos(270,-230)


chess_pieces()
