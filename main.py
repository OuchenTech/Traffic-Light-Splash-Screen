from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '665')
from kivymd.app import MDApp

from screens.homescreen.homescreen import HomeScreen
from screens.splashscreen.splashscreen import SplashScreen

class MainApp(MDApp):
    def build(self):
        self.title = "Traffic Light Splash"
        
    def on_start(self):
        self.root.current = 'splash_screen'
        
        
if __name__ == "__main__":
    MainApp().run()