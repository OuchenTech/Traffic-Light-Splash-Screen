from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ColorProperty
from kivy.clock import Clock

class TrafficLightLayout(MDFloatLayout):
    bg_color = ColorProperty()
    initial_bg_color = ColorProperty()
    
    def __init__(self, **kwargs):
        super(TrafficLightLayout, self).__init__(**kwargs)
        self.bg_color = [238/255, 241/255, 250/255, 1]
        self.initial_bg_color = [238/255, 241/255, 250/255, 1]
        
    def change_background_color(self, color):
        self.bg_color = color
        
    def reset_background_color(self):
        self.bg_color = self.initial_bg_color

class SplashScreen(Screen):
    
    def change_first_light_color(self, *args):
        light1 = self.ids.light1
        light1.change_background_color([240/255, 55/255, 60/255, 1]) #Red Color
        
    def change_second_light_color(self, *args):
        light1 = self.ids.light1
        light1.reset_background_color()
        light2 = self.ids.light2
        light2.change_background_color([255/255, 202/255, 15/255, 1]) #Yellow Color
        
    def change_third_light_color(self, *args):
        light2 = self.ids.light2
        light2.reset_background_color()
        light3 = self.ids.light3
        light3.change_background_color([71/255, 226/255, 111/255, 1]) #Green Color
        
    def to_home(self, *args):
        self.manager.current = 'home_screen'
        
        
    def on_enter(self, *args):
        Clock.schedule_once(self.change_first_light_color, 3)
        Clock.schedule_once(self.change_second_light_color, 4)
        Clock.schedule_once(self.change_third_light_color, 5)
        Clock.schedule_once(self.to_home, 6)
        
        
        
        
        
        
        
        
        
        
        