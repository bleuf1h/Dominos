#FINAL PROJECT DOMINO REPLICA
#this code is from a few days ago, from the old repository i am going to fix it later today

import flet as ft
import random
class DominoGame:
    def __init__(self, page: ft.Page): #I created a class instead of doing 67 variables but might change it ngl cuz i kinda dont like it
        self.status = ft.Text(size=20, weight=ft.FontWeight.BOLD)
        self.mesa_ui = ft.Row(scroll=ft.ScrollMode.AUTO)
        self.player_ui = ft.Row(wrap=True)
        self.npc_ui = ft.Text(size=18)
        self.score_ui = ft.Text(size=18)       

def main(page: ft.Page):
        
        
    #      ------ FUNCTIONS ------

        def create_dominoes(): #create the pieces (1) // DONE (ISABEL)
              return [(a, b) for a in range(7) for b in range(a, 7)]
        
        def new_game(): #creates the game (2)
               pass
        
        def shuffle_dominoes(self): #shuffle domino (3)567l,-6
               pass
        
        def place(): #game logic (check left check right etc etc etc) (4)
               pass
        
        def left_value(self): #the value on the left side of the domino (5) // DONE (ISABEL)
               return self.mesa[0][0]

        def right_value(self): #the value on the right side of the domino (6) // DONE (ISABEL)
               return self.mesa[-1][1]
        
        def play_player(self): #checks if the player can play, valga la redundancia (7) (ISABEL)
               pass
        
        def npc_player (self): #npc playing idek (8)
               pass
        
        def draw_tile(self, e): #self explainatory (9)
               pass
        
        def refresh(e): #self explainatory aswell (10)
               pass



    # ------ more CONTROLS ------ (ISABEL)
    

    #---- PAGE SETUP ----- 

ft.run(main=main)
