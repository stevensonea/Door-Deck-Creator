import pandas as pd

class File_Reader:

    def __init__(self, filePath) :
        self.source = filePath
        self.names = []
        self.pictureNames = []

    def findOptions(self):
        try:
            data = pd.read_csv(self.source)
            row1 = data.loc[0]
            print(row1)
            #for i, j in data.iloc[0]:
                
                #print (i, j)
                #self.names.append(name)
                #self.pictureNames.append(pictureName)

        
        except IOError:
            print ("Invalid File Path!")

        except:
            print ("An unexpected error occured, please try again")
        
    def showData(self):
        for i in range(len(self.names)):
            print(f"{self.names[i]}, {self.pictureNames[i]}")


        
        
