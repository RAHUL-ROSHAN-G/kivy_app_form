from tkinter.tix import ButtonBox
import sys
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        self.cols = 2 #column
        self.add_widget(Label(text = 'Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text = 'Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text = 'Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = 'Click me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

        self.press = Button(text = 'EXIT')
        self.press.bind(on_press = self.exit_out)
        self.add_widget(self.press)

    def click_me(self,instance):
        print("Name of the Student is: "+self.s_name.text)
        print("Marks of the Student is: "+self.s_marks.text)
        print("Gender of the Student is: "+self.s_gender.text)
        print("")

    def exit_out(self,instance):
        sys.exit()



class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()
