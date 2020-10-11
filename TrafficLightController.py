# Required libraries and modules
from time import sleep
import logging
from tkinter import *

# Traffic Light's class
class TrafficLight:
    def __init__(self):
        '''Constructor'''
        
        self.lights = ["", "", ""]

    def __check_user_input(self, u_input):
        '''Checking for user input error'''
        
        try:
            if u_input in ["green","yellow","red"]:
                return u_input
        except NameError:
            logging.error(" NameError: Undefined variable. Enter a string 'green', 'yellow, or 'red'")
        except TypeError:
            logging.error(" TypeError: Incorrect data type. Enter a string 'green', 'yellow, or 'red'")

    def change_light(self, light):
        '''Changing the light sequence accorging to user input'''
        
        light_select = self.__check_user_input(light)

        if light_select == 'green':
            self.lights = ["", "", "green"]
        elif light_select == 'yellow':
            self.lights = ["", "yellow", ""]
        else:
            self.lights = ["red", "", ""]

    def alert(self):
        '''Additional sequence in case that there is an internal error in the traffic light'''
        
        self.lights = ["", "", ""]
        sleep(2)
        self.lights = ["red", "", ""]
        sleep(2)

    def off(self):
        '''Turns off the three lights of the traffic light'''
        
        self.lights = ["", "", ""]
        

# Traffic Light Controller class
class TrafficLightController(TrafficLight):

    def __init__(self):
        '''Constructor'''
        
        # Intialization of attributes as objects of the TrafficLight class
        self.TF1 = TrafficLight()
        self.TF2 = TrafficLight()
        self.TF3 = TrafficLight()
        self.TF4 = TrafficLight()
        self.states = {"S1":["green","red","green","red",14],
                       "S2":["yellow","red","yellow","red",6],
                       "S3":["red","green","red","green",14],
                       "S4":["red","yellow","red","yellow",6],
                       "SM":["red","red","red","red",3]}
        
        # Creation and initialization of the GUI's window
        self._controller_display = Tk()
        self._controller_display.title("Controller Display")
        self._controller_display.geometry("600x350")
        self._display = Canvas(self._controller_display,width=800, height=800)
        
        # Generation of lights for traffic lights as private attributes
        self._TF1_LR = self._display.create_oval(20,20,100,100,outline='black')
        self._TF1_LY = self._display.create_oval(20,120,100,200,outline='black')
        self._TF1_LG = self._display.create_oval(20,220,100,300,outline='black')
        self._TF2_LR = self._display.create_oval(160,20,240,100,outline='black')
        self._TF2_LY = self._display.create_oval(160,120,240,200,outline='black')
        self._TF2_LG = self._display.create_oval(160,220,240,300,outline='black')
        self._TF3_LR = self._display.create_oval(300,20,380,100,outline='black')
        self._TF3_LY = self._display.create_oval(300,120,380,200,outline='black')
        self._TF3_LG = self._display.create_oval(300,220,380,300,outline='black')
        self._TF4_LR = self._display.create_oval(440,20,520,100,outline='black')
        self._TF4_LY = self._display.create_oval(440,120,520,200,outline='black')
        self._TF4_LG = self._display.create_oval(440,220,520,300,outline='black')
        # Including the display (canvas) in the application's window
        self._display.pack()

    def change_color(self):
        '''Changing the color of the 12 lights'''
        
        self._display.itemconfig(self._TF1_LR, fill=self.TF1.lights[0])
        self._display.itemconfig(self._TF1_LY, fill=self.TF1.lights[1])
        self._display.itemconfig(self._TF1_LG, fill=self.TF1.lights[2])
        self._display.itemconfig(self._TF2_LR, fill=self.TF2.lights[0])
        self._display.itemconfig(self._TF2_LY, fill=self.TF2.lights[1])
        self._display.itemconfig(self._TF2_LG, fill=self.TF2.lights[2])
        self._display.itemconfig(self._TF3_LR, fill=self.TF3.lights[0])
        self._display.itemconfig(self._TF3_LY, fill=self.TF3.lights[1])
        self._display.itemconfig(self._TF3_LG, fill=self.TF3.lights[2])
        self._display.itemconfig(self._TF4_LR, fill=self.TF4.lights[0])
        self._display.itemconfig(self._TF4_LY, fill=self.TF4.lights[1])
        self._display.itemconfig(self._TF4_LG, fill=self.TF4.lights[2])
        self._display.update()
        
    def state(self, value):
        '''Verifying if the specified state exists and change attributes of the TrafficLight accordingly'''
        
        if value in self.states.keys():
            # Obtain colors from the public attribute states (dictionary)
            self.TF1.change_light(self.states[value][0])
            self.TF2.change_light(self.states[value][1])
            self.TF3.change_light(self.states[value][2])
            self.TF4.change_light(self.states[value][3])
            # Updating color in the GUI
            self.change_color()
            # Obtain waiting time from the public attribute states (dictionary)
            sleep(self.states[value][4])
        else:
            logging.error("Invalid state")

    def sequence(self):
        '''Default sequence'''
        
        self.state("S1")
        self.state("S2")
        self.state("SM")
        self.state("S3")
        self.state("S4")
        self.state("SM")
        
    def terminate(self):
        '''Closes the application's automatically'''
        
        self._controller_display.destroy()
        
        
# Main program
TLC = TrafficLightController()
TLC.sequence()
TLC.terminate()
