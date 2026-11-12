#importation de toute les bibliotheque nécessaire 
from faulthandler import disable
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

#parametrage du la taille de l'application
Window.size = (360,800)
#suite à décommenter lors de la compilation du programe
#Window.maximize()

class LetterInput(TextInput):
    """Case ne contenant qu'une seul lettre."""
    
    def __init__(self, **kwargs):
        super().__init__(
            multiline = False,
            halign = "center",
            font_size = "20sp",
            write_tab = False,
            **kwargs,
        )
        self.next_input = None
        self.prev_input = None
        
    def insert_text(self,substring,from_undo = False):
        lettre = "".join(c for c in substring if c.isalpha())[:1].upper()
        if not lettre:
            return super().insert_text("",from_undo=from_undo)
        self.text = ""
        resultat = super().insert_text(lettre,from_undo=from_undo)
        if self.next_input:
            Clock.schedule_once(lambda dt: setattr(self.next_input, "focus", True),0)
        return resultat
    
    def keyboard_on_key_down(self,window,keycode,text,modifiers):
        if keycode[1] == "backspace":
            if self.text:
                self.text = ""
            elif self.prev_input:
                self.prev_input.text = ""
                Clock.schedule_once(lambda dt: setattr(self.prev_input,"focus",True),0)
            return True
        return super().keyboard_on_key_down(window,keycode,text,modifiers)
    
    
class Motus():
    def __init__(self, **kwargs):
        super(Motus,self).__init__(**kwargs)
    
    def main():
        #creation d'une boite qui contiendra tous les éléments du jeu
        MainBox = BoxLayout(orientation = 'vertical')

        #creation et ajout du nom de l'applicationen haute de l'écran
        TitleLabel = Label(text='Motus')
        MainBox.add_widget(TitleLabel)


        '''
        for column in range(6):
            TryLabel2 = BoxLayout(orientation = 'horizontal')
            cases = [LetterInput() for _ in range(5)]
            for i,case in enumerate(cases):
                if i>0:
                    case.prev_input = cases[i-1]
                if i < len(cases) -1:
                    case.next_input = cases[i+1]
                TryLabel2.add_widget(case)
            MainBox.add_widget(TryLabel2)
        '''

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
