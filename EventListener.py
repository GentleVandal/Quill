from Parser import Parser
import keyboard 
from threading import Thread
from Tkinter import *




class EventListener:

    def __init__(self,parser,scrolledText):
        
        self.parser = parser
        self.keybThread = Thread(target=keyboard.on_press(self.listen),name="Keyboard Hook Thread")
        self.scrolledText = scrolledText
        self.startRow = 1
        self.startIndex = 0
        

    def startKeyboardThread(self):
        self.keybThread.start()

    def listen(self,obj):
        
        if obj.name == "space":
            #Text.get(self, index1, index2=None)
            #Return the text from INDEX1 to INDEX2 (not included).
            self.parser.parseString = self.scrolledText.get("%s.%s"%(startRow,startIndex),INSERT)
            self.startIndex = INSERT
            parseThread = Thread(target=self.parser.compare(self.parser.parseString))
            parseThread.start()

        elif obj.name == "enter":
            self.startRow += 1
            self.startIndex = INSERT
            
        elif obj.name == "backspace":
            self.startIndex = INSERT
            #Check if cursor is on the first line.
            #There can be some situations which user is already at the beginning and is pressing backspace
            if self.startIndex == END and self.startRow != 1:
                self.startRow -= 1
            
            
             
            


        
