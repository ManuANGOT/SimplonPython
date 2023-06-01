from tkinter import Tk, Canvas, Label, StringVar, Button, OptionMenu, DISABLED, NORMAL
from PIL import Image, ImageTk
import random

# cf https://www.mathweb.fr/euclide/2021/09/13/creer-le-jeu-du-morpion-en-python/

# Création fenêtre du jeu
class Morpion:
    def __init__(self, window):
        window.geometry("750x505")
        window.title("Le jeu du Morpion - Emmanuel ANGOT (Test Simplon Roubaix 2023)")
        Label(window, text="Le jeu du Morpion (OXO)", font=("Helvetica", 20)).place(x=190,y=1)
        
        self.game = Canvas(window, width = 405, height = 405, bg = "white")        

# ajout des menus       
        Label(text="Quel niveau ?", font=('Helvetica', 12), fg='red').place(x = 420, y = 50)
        self.LevelList = [ "?????" , "Facile", "Difficile" ]
        self.LevelVar = StringVar(window)
        self.LevelVar.set(self.LevelList[0])
        self.LevelOptions = OptionMenu(window, self.LevelVar, *self.LevelList)
        self.LevelOptions.config(width = 10, font=('Helvetica', 12))
        self.LevelOptions.place(x = 600 , y = 44)
        self.niveau = self.LevelVar.trace("w", self.jeu)
    
        Label(text="Qui commence à jouer ?", font=('Helvetica', 12), fg='red').place(x = 420, y = 100)
        self.FirstPlayerList = [ "?????" , "Joueur", "Ordinateur" ]
        self.FirstPlayerVar = StringVar(window)
        self.FirstPlayerVar.set(self.FirstPlayerList[0])
        self.FirstPlayerOptions = OptionMenu(window, self.FirstPlayerVar, *self.FirstPlayerList)
        self.FirstPlayerOptions.config(width = 10, font=('Helvetica', 12))
        self.FirstPlayerOptions.place(x = 600 , y = 94)
        self.player_one = self.FirstPlayerVar.trace("w", self.jeu)
        
        # bouton "rejouer"
        self.rejouer = Button(window , text = 'Rejouer' , state=DISABLED , command=self.restart)
        self.rejouer.place(x = 560 , y = 400)
        
        # bouton "Statistiques"
        self.stats = Button(window , text = 'Afficher les statistiques'  , command=self.visu_stats)
        self.stats.place(x = 530 , y = 450)

        # création des symboles joueurs X et O
        self.image_croix = Image.open("croix.png")
        self.croix = ImageTk.PhotoImage(self.image_croix)
        
        self.image_cercle= Image.open("cercle.png")
        self.cercle = ImageTk.PhotoImage(self.image_cercle)
        
        self.text_gamer = StringVar()
        self.texte_joueur = Label(root , textvariable=self.text_gamer , font=('Helvetica', 12), fg='blue').place(x = 420, y = 150)
        
        self.text_result = StringVar()
        self.texte_result = Label(root , textvariable=self.text_result , font=('Helvetica', 12), fg='purple').place(x = 420, y = 200)

if __name__ == '__main__':    
    root = Tk()
    Morpion(root) 

# création de la grille    
def draw_grid(self):
        self.game.create_rectangle(0,0,405,405,fill='white')
        for x in [ 4 , 135 , 270 , 405 ]:
            self.game.create_line(0 , x , 405 , x , fill = 'black' , width = 4)
            self.game.create_line(x , 0 , x , 405 , fill = 'black' , width = 4)
        
        self.game.place(x = 0 , y = 50)   

# ajout de la ligne dans le constructeur
self.draw_grid()

# ajout des méthodes pour les boutons
def jeu(self):
        return None
    
def restart(self):
        return None
    
def visu_stats(self):
        return None


self.restart() # initialisation