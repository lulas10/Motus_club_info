"""
    Fichier principal de la branche d'Alper pour l'application mobile Motus.
"""
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp

IMAGE_PATH = "button_image\\"
NB_ESSAI = 6
NB_LETTRE = 5

class Case(Button):
    def __init__(self, **kwargs):
        super().__init__(
            disabled = True,
            disabled_color = (1,1,1,1),
            font_size = "32sp",
            **kwargs,
        )

class Motus(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical",**kwargs)
        self.ligne = 0
        self.colone = 0
        self.grille = []

        self.add_widget(Label(text = "Motus"))

        #grille de tentatives
        for _ in range(NB_ESSAI):
            ligne = BoxLayout(orientation = "horizontal")
            cases = [Case() for _ in range(NB_LETTRE)]
            for case in cases:
                ligne.add_widget(case)
            self.grille.append(cases)
            self.add_widget(ligne)

        #clavier virtuelle
        clavier = BoxLayout(orientation="vertical",size_hint_y = 1.4)
        chaine_lettre_bouton = ["azertyuiop","qsdfghjklm","wxcvbn"]
        for i, lettres in enumerate(chaine_lettre_bouton):
            ligne = BoxLayout(orientation = "horizontal")
            if i == 2: # ajoute le bouton pour effacer au début de la deuxième colone
                ligne.add_widget(self.bouton_image("backspace", self.effacer_lettre,size_hint_x = 2))
            for lettre in lettres:
                ligne.add_widget(self.bouton_image(lettre, lambda btn, l=lettre: self.ajouter_lettre(l)))
            if i == 2:
                ligne.add_widget(self.bouton_image("valider", self.valider,size_hint_x=2))
            clavier.add_widget(ligne)
        self.add_widget(clavier)

    def bouton_image(self, nom, action, **kwargs):
        bouton = Button(
            background_normal= IMAGE_PATH + nom + "_light.png",
            **kwargs,
        )
        bouton.bind(on_press=action)
        return bouton

    def ajouter_lettre(self, lettre):
        if self.ligne < NB_ESSAI and self.colone < NB_LETTRE:
            self.grille[self.ligne][self.colone].text = lettre.upper()
            self.colone+=1
    
    def effacer_lettre(self, *args):
        if self.colone > 0:
            self.colone -= 1
            self.grille[self.ligne][self.colone].text = ""
    
    def valider(self, *args):
        if self.colone == NB_LETTRE:
            self.grille[ligne][colone].background_color = [255,0,0,1]
            # A faire : vérification du mot
            self.ligne += 1
            self.colone = 0



if __name__ == "__main__":
    Window.size = (360,800)
    runTouchApp(Motus())
