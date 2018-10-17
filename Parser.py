#from DatabaseManager import *
#from Editor import *

class Parser:

    def __init__(self,dbManager,editor):
        self.dbManager = dbManager
        self.parseString = " "
        self.editor = editor
        
        
    def highlight(source):
        # Make word <source> clickable and use it when user clicks: 
        #self.editor.openWidget(result)
        pass
        
        
        
    def compare(self,source):
        result = self.dbManager.query(source)
        if result[0] == 1:
            self.highlight(source)
            return 1
        elif result[0] == 0:
            return 0
