import flet as ft
import flet_audio as fta
import random
#-----------------------------------------------------------------------------
#CONTROLS INSIDE A CLASS (CONTROLS)

class DOMINO_GAME:
    def __init__(self, page):
        self.page = page
        self.page.title = "DOMINO"
        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.player_status = ft.Text(size=20)
        self.turn_counter = ft.Text(size=18)
        self.board_text = ft.Text(size=25)
        self.npc_text = ft.Text(size=18)
        self.player_row = ft.Row()
        self.draw_button = ft.ElevatedButton ("Draw Tile", on_click= self.draw_tile)

#-----------------------------------------------------------------------------
#AUDIO AND IMAGES (CONTROLS)
        self.audio_player = fta.Audio (src = "audio/Main Menu.mp3", autoplay=True)
        self.front_page = ft.Image(src= "assets/images/frontpage.webp")

#-----------------------------------------------------------------------------
#WELCOME PAGE (PAGE SETUP)
        self.welcome()

    def start_button_click(self, e):
        self.start_game()

    def welcome(self):
            self.page.controls.clear()

            title = ft.Text(
                "DOMINOES",
                size=40,
                weight=ft.FontWeight.BOLD
            )

            subtitle = ft.Text(
                "Player vs NPC",
                size=20
            )

            start_button = ft.ElevatedButton(
                "START GAME",
                on_click=self.start_button_click,
                width=200,
                height=50
            )

            self.page.add(
                ft.Column(
                    [
                        self.front_page,
                        title,
                        subtitle,
                        start_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            )

            self.page.update()

#-----------------------------------------------------------------------------
#WINLOSS SCREEN (PAGE SET UP)
    def win_screen (self): #WINNER SIDE 

        self.audio_player.src = "audio/IJUSTHITTHEJACKPOT.m4a"
        win_image = ft.Image(src="images/feels-the-aura.png", width=400)

        self.page.controls.clear() 
        self.page.add(ft.Column(
                [ft.Text("PLAYER WINS!",
                        size=40,
                        weight=ft.FontWeight.BOLD),

                    win_image,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ))
        self.page.update ()

    def loser_screen (self): #LOSER SIDE (Take the L)
        self.page.controls.clear() 
        self.audio_player.src = "audio/LOSER.m4a"
        lose_image = ft.Image(src="images/unfeels_the_aura.png", width=400)
        self.page.add(ft.Column(
                [ft.Text("NPC WINS! YOU LOSE!",
                        size=40,
                        weight=ft.FontWeight.BOLD),

                    lose_image,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ))
        self.page.update ()
#-----------------------------------------------------------------------------
#DEVELOPING THE ACTUAL COMPONENTS OF THE GAME(FUNCTIONS)
    def create_domino_tiles(self): 
        tiles = []
        for i in range(7):  #Basically this is 0,1,2,3,4,5,6, so i becomes 0 then one etc. yadadayada yada
            for j in range(i,7):    #This goes along with i so whatever number i is it just goes along with it.
                tiles.append((i,j)) 
        return tiles
    
    def start_game(self):
        self.deck = self.create_domino_tiles()
        random.shuffle(self.deck)

        self.player = self.deck[0:7]    #Gives the player the first seven tiles on the deck
        self.npc = self.deck[7:14]      #Gives the npc the next seven tiles
        self.deck = self.deck[14: ]     #The remaining tiles all stay in the deck

        self.board = []
        self.turn = "Player turn"
        self.update_game()
    
    def update_game(self):                                      #DONE
        self.turn_counter.value = self.turn
        self.board_text.value = str(self.board)
        self.npc_text.value = (f"NPC tiles {len(self.npc)}")    #I used len here bc it counts the amount of tiles
        self.player_status.value = (f"You have this much remainding tiles: {len(self.player)}") #Same here

        self.player_row.controls.clear()
        for tile in self.player:
            button = ft.ElevatedButton(str(tile), on_click=self.create_click(tile))
            self.player_row.controls.append(button)

        self.page.controls.clear()  #Removes EVERYTHING from the page
        self.page.add(
            ft.Text("DOMINO", size=40, weight=ft.FontWeight.BOLD),
            self.turn_counter,
            self.player_status,
            self.npc_text,
            self.board_text,
            self.player_row,
            self.draw_button
        )
        self.page.update()
#-----------------------------------------------------------------------------
#PLAYING DYNAMICS START HERE (FUNCTIONS)
    def play_tile(self, tile):
        if not self.can_play(tile):
            self.player_status.value = "Invalid Move"
            self.update_game()
            return
        
        self.place_tile(tile)
        self.player.remove(tile)

        if len(self.player) == 0: #Added winning conditionals
            self.win_screen()
            return

        if len(self.npc) == 0: 
            self.loser_screen()
            return
        
        self.turn = "NPCs Turn"
        self.update_game()
        self.npc_turn()
    
    def create_click(self, tile):
        def click(e):
            self.play_tile(tile)
        return click

    def npc_turn(self):             #OJO: The npc is dumb for now 
                                    #UPDATE BRO IS NOT DUMB ANYMORE: DO NOT CHANGE THIS FUNCTION ITS ALREADY WORKING
                                    #NEVERMINDD HAHAHAHAHHA
                                    #NPC IS NOT DUMB ANYMORE, HOWEVER IT'S PASSING FOREVER#OJO: The npc is dumb for now
        while not self.has_playable_tile(self.npc) and len(self.deck) > 0: #FIXED this so its draws the tile properly
            try:
                drawn_tile = self.deck.pop()
                self.npc.append(drawn_tile)
            except IndexError:
                self.player_status.value = "No tiles in deck."

        for tile in self.npc:
            if self.can_play(tile):
                self.place_tile(tile)
                self.npc.remove(tile)

                # WIN CONDITION
                if len(self.npc) == 0:
                    self.turn = "NPC Wins!!!"
                else:
                    self.turn = "Player Turn"

                self.update_game()
                return

    
    def can_play(self, tile):          #This variable is mainly so that the npc can follow the main game mechanics and not just put the first tile it sees.
        if len(self.board) == 0:
            return True
        
        left_side = self.board[0][0]
        right_side = self.board[-1][1]
        x = tile[0]
        y = tile[1]

        if (
            x == left_side or 
            y == left_side or 
            x == right_side or 
            y == right_side
        ):
            return True
        return False
    
    def place_tile(self, tile):
        if len(self.board) == 0:
            self.board.append(tile)
            return
        left_side = self.board[0][0]
        right_side = self.board[-1][1]

        x = tile[0]
        y = tile[1]

        if x == right_side:
            self.board.append((x,y))
        elif y == right_side:
            self.board.append((y,x))
        elif y == left_side:
            #SO for the left side I put zero at the start of the thingy so that it puts it at the START of the list.
            self.board.insert(0,(x,y))
        elif x == left_side:
            self.board.insert(0,(y,x))

#-----------------------------------------------------------------------------
#THIS IS WHERE THE DRAWING LOGISTICS START (WE ARE STILL IN FUNCTIONS)
    def has_playable_tile(self, hand):
        for tile in hand:
            if self.can_play(tile):
                return True
        return False
   
    def draw_tile (self, e): #Tells you if you need to draw a tile basically
        if self.has_playable_tile(self.player):
            self.player_status.value = "You already have a playable tile :)" #Playable Tile
            self.update_game()
            return
        
        #Empty Deck
        if len(self.deck) == 0:
            self.player_status.value = "Deck is empty."
            self.update_game ()
            return

        drawn_tile = self.deck.pop() 
        self.player.append(drawn_tile)
        self.update_game ()

        self.player_status.value = f"You Drew {drawn_tile}"
#-----------------------------------------------------------------------------
#MAKE IT GORGEOUS (PAGE SETUP)

#-----------------------------------------------------------------------------
#PAGE

def main(page: ft.Page):
    DOMINO_GAME(page)
ft.run(target=main,  assets_dir="assets")