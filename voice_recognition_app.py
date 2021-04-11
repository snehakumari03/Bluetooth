from kivy.uix.screenmanager import Screen , ScreenManager
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.font_definitions import theme_font_styles
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDRaisedButton
import speech_recognition as sr
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.picker import MDThemePicker


Window.size = (300, 500)

r = sr.Recognizer()

helper = '''
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "kivymd.png"
    MDLabel:
        text: 'App Menu'
        font_style: 'Subtitle1'
        size_hint_y: None
        height: self.texture_size[1]
                        

    MDLabel:
        text: 'Version 1.01'
        font_style: 'Caption'
        size_hint_y: None
        height: self.texture_size[1] 
                

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Home Page"
                
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "About"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            
            OneLineListItem:
                text: "Settings"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
            
        


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 8
        title: "Voice To Text"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDBottomAppBar:
        MDToolbar:
            title: 'Start'
            mode: 'end'
            icon: 'microphone'
            type: 'bottom'
            on_action_button:app.record()
            elevation:8
    
        
    NavigationLayout:
        x: toolbar.height        
        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text:"Say Something"
                    halign: "center"

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "About App"
                    halign:"center"
            Screen:
                name: "scr 3"
                MDRoundFlatButton:
                    text:'Change Theme of App'
                    pos_hint:{'center_x':0.5, 'center_y':0.5}
                    on_release:app.show_theme_picker()
                            
                    
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

        
'''
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    

class MainApp(MDApp):
    
    def build(self):

        
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Light"
        screen = Builder.load_string(helper)
        return screen
    
    def record(self):
        
           with sr.Microphone() as source:
               print("Say something");
               while True:
                    audio = r.listen(source)
                    print(" ")
                    try:
                    
                        print(r.recognize_google(audio));
                    except:
                        pass;
                
    def show_theme_picker(self):
            theme_dialog = MDThemePicker()
            theme_dialog.open()

MainApp().run()

