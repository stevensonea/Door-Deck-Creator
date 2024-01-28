from reader import File_Reader

tester_pass = File_Reader("testFiles/resident.xlsx")
tester_fail = File_Reader("testFiles/residenwt.xlsx")

tester_pass.findOption()
tester_fail.findOption()
