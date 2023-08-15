import pandas

class ExcelReader:
    def __init__ (self, fileName):
        self.fileName = fileName
        self.names = []
        self.fontSize = []
        self.pictures = []

    def readFile (self):
        