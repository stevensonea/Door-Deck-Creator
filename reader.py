import pandas as pd

class File_Reader:

    def __init__(self, filePath) :
        self.source = filePath

    def findOption(self):
        try:
            data = pd.read_csv(self.source)
        
        except IOError:
            print ("Invalid File Path!")
        
        print("Success!")
