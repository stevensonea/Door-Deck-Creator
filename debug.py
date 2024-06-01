from reader import File_Reader

tester_pass = File_Reader("testFiles/resident.csv")
tester_fail = File_Reader("testFiles/residenwt.xlsx")

tester_pass.findOptions()

#tester_pass.showData()