__version__ = '0.2'

# Program to create a calculator 

# import kivy module    
import kivy

# base Class of your App inherits from the App class.    
# app:always refers to the instance of your application   
from kivy.app import App 
     
# this restrict the kivy version i.e  
# below this kivy version you cannot  
# use the app or software  
kivy.require('1.9.0') 
  
# for making multiple bttons to arranging
# them we are using this
from kivy.uix.gridlayout import GridLayout
  
# for the size of window
from kivy.config import Config
  
# Setting size to resizable
Config.set('graphics', 'resizable', 1)
## Config.set('graphics', 'width', '400')
## Config.set('graphics', 'height', '400')

	
# Creating Layout class
class CalcGridLayout(GridLayout):
   
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = calculate_execution(calculation)
            except Exception:
                self.display.text = "Error"

def calculate_execution(calculation):
    result = str(eval(calculation))
    float_result = round(float(result), 6)
    if float_result.is_integer():
        result = str(int(float_result))
    else:
        result = str(float_result)
    return result
   
 # Creating App class
class CalculatorApp(App):
   
    def build(self):
        self.icon = 'data/icon.png'
        return CalcGridLayout()
   
# creating object and running it
if __name__ == '__main__':
    calcApp = CalculatorApp()
    calcApp.run()
