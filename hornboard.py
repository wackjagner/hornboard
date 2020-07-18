import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.utils import get_color_from_hex
kivy.require("1.11.1")

class boardPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.color1 = get_color_from_hex('#c1dbdf')
        self.color2 = get_color_from_hex('#FFB6C1')
        Window.clearcolor = (self.color1)

        def buttonPressOne():
            self.horn1=SoundLoader.load('horn1.wav')
            self.horn1.play()
        
        def buttonPressTwo():
            self.horn2=SoundLoader.load('horn2.wav')
            self.horn2.play()

        def buttonPressThree():
            self.horn3=SoundLoader.load('horn3.wav')
            self.horn3.play()
        
        def buttonPressFour():
            self.horn4=SoundLoader.load('horn4.wav')
            self.horn4.play()

        def buttonPressFive():
            self.harp1=SoundLoader.load('harp1.wav')
            self.harp1.play()
        
        def buttonPressSix():
            self.harp2=SoundLoader.load('harp2.wav')
            self.harp2.play()

        def buttonPressSeven():
            self.curse=SoundLoader.load('curse.wav')
            self.curse.play()

        def buttonPressEight():
            self.cemetary=SoundLoader.load('cemetary.wav')
            self.cemetary.play()

        def buttonPressNine():
            self.whistleUp=SoundLoader.load('whistleUp.wav')
            self.whistleUp.play()

        def buttonPressTen():
            self.whistleDown=SoundLoader.load('whistleDown.wav')
            self.whistleDown.play()

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label(text="[b]Hornapp[/b] by Jack Wagner", markup=True))
        self.add_widget(Label())
        self.add_widget(Label())

        self.soundOne=Button(background_color=(.32, .54, 1.86, .23), text="horn 1")
        self.soundOne.bind(on_press=lambda x:buttonPressOne())
        self.add_widget(self.soundOne)
        self.soundTwo=Button(background_color=(.32, .54, 1.86, .23), text="horn 2")
        self.soundTwo.bind(on_press=lambda x:buttonPressTwo())
        self.add_widget(self.soundTwo)
        self.soundThree=Button(background_color=(.32, .54, 1.86, .23), text="horn 3")
        self.soundThree.bind(on_press=lambda x:buttonPressThree())
        self.add_widget(self.soundThree)
        self.soundFour=Button(background_color=(.32, .54, 1.86, .23), text="r e v e r b")
        self.soundFour.bind(on_press=lambda x:buttonPressFour())
        self.add_widget(self.soundFour)
        self.soundFive=Button(background_color=(.32, .54, 1.86, .23), text="jaw harp\n1")
        self.soundFive.bind(on_press=lambda x:buttonPressFive())
        self.add_widget(self.soundFive)

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.soundSix=Button(background_color=(.32, .54, 1.86, .23), text="jaw harp\n2")
        self.soundSix.bind(on_press=lambda x:buttonPressSix())
        self.add_widget(self.soundSix)
        self.soundSeven=Button(background_color=(.32, .54, 1.86, .23), text="c u r\ns e")
        self.soundSeven.bind(on_press=lambda x:buttonPressSeven())
        self.add_widget(self.soundSeven)
        self.soundEight=Button(background_color=(.32, .54, 1.86, .23), text="c e m e\nt a r y")
        self.soundEight.bind(on_press=lambda x:buttonPressEight())
        self.add_widget(self.soundEight)
        self.soundNine=Button(background_color=(.32, .54, 1.86, .23), text="slide\nwhistle\nup")
        self.soundNine.bind(on_press=lambda x:buttonPressNine())
        self.add_widget(self.soundNine)
        self.soundTen=Button(background_color=(.32, .54, 1.86, .23), text="slide\nwhistle\ndown")
        self.soundTen.bind(on_press=lambda x:buttonPressTen())
        self.add_widget(self.soundTen)

class MyApp(App):

    def build(self):
        return boardPage()


if __name__ == '__main__':
    MyApp().run()