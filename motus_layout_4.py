"""
    Fichier principal de la branche d'Alper pour l'application mobile Motus.
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
# On importe les éléments nécessaires de la bibliothèque kivy.

# Parametrage du la taille de l'application.
Window.size = (350,700)

def main():
    """
        Créer la fenêtre de l'écran pour le jeu.

        Entrée : Aucune.

        Sortie : Aucune.
    """
    # Création d'une boîte qui contiendra tout les éléments du jeu.
    MainBox = BoxLayout(orientation = 'vertical')

    # Création et ajout du nom de l'application en haut de l'écran.
    TitleLabel = Label(text='Motus')
    MainBox.add_widget(TitleLabel)

    #Clock.schedule_once(lambda dt: setattr(cases[0], "focus",True),0.2)

    for column in range(6):
        TryLabel = BoxLayout(orientation = 'horizontal')
        cases = [Button(disabled=True) for _ in range(5)]
        for i,case in enumerate(cases):
            TryLabel.add_widget(case)
        MainBox.add_widget(TryLabel)
    
    KeyboardLabel = BoxLayout(orientation='vertical')
    chaine_lettre_bouton = 'azertyuiopqsdfghjklmwxcvbn'
    variant_choix_lettre = 0
    for rows in range(2):
        row = BoxLayout(orientation='horizontal')
        for i in range(10):
            row.add_widget(Button(text=chaine_lettre_bouton[variant_choix_lettre],background_color=[0,255,0,1]))
            variant_choix_lettre+=1
        KeyboardLabel.add_widget(row)
    
    row = BoxLayout(orientation='horizontal')
    row.add_widget(Button(text='<-',size_hint_x = 2))
    for i in range(6):
            row.add_widget(Button(text=chaine_lettre_bouton[variant_choix_lettre],background_color=[0,255,0,1]))
            variant_choix_lettre+=1
    row.add_widget(Button(text='Valider',size_hint_x = 2))
    KeyboardLabel.add_widget(row)
    
    MainBox.add_widget(KeyboardLabel)

    return MainBox

class MainApp(App):
    def build(self):
        return Motus.main()

if __name__ == "__main__":
    MainApp().run()
