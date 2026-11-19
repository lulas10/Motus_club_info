"""
    Fichier principal de la branche d'Alper pour l'application mobile Motus.
"""
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp

def main() -> BoxLayout:
    """
        Créer la fenêtre de l'écran pour le jeu.

        Entrée : Aucune.

        Sortie : Aucune.
    """
    Window.size = (350, 700)
    main_box: BoxLayout = BoxLayout(orientation = 'vertical')
    main_box.add_widget(Label(text = 'Motus'))
    for _ in range(6):
        try_label: BoxLayout = BoxLayout(orientation = 'horizontal')
        cases = [Button(disabled = True) for _ in range(5)]
        for _, case in enumerate(cases):
            try_label.add_widget(case)
        main_box.add_widget(try_label)
    keyboard_label: BoxLayout = BoxLayout(orientation = 'vertical')
    chaine_lettre_bouton: str = 'azertyuiopqsdfghjklmwxcvbn'
    variant_choix_lettre: int = 0
    for _ in range(2):
        row: BoxLayout = BoxLayout(orientation = 'horizontal')
        for _ in range(10):
            row.add_widget(Button(text = chaine_lettre_bouton[variant_choix_lettre], background_color = [0, 255, 0, 1]))
            variant_choix_lettre += 1
        keyboard_label.add_widget(row)
    row: BoxLayout = BoxLayout(orientation = 'horizontal')
    row.add_widget(Button(text = '<-', size_hint_x = 2))
    for _ in range(6):
        row.add_widget(Button(text = chaine_lettre_bouton[variant_choix_lettre], background_color = [0, 255, 0, 1]))
        variant_choix_lettre += 1
    row.add_widget(Button(text = 'Valider', size_hint_x = 2))
    keyboard_label.add_widget(row)
    main_box.add_widget(keyboard_label)
    return main_box

if __name__ == "__main__":
    runTouchApp(main())
