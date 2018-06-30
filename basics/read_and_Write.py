with open('test.log', mode='a') as a_file:
    a_file.write('test succeeded')                            

with open('test.log') as a_file:
     print(a_file.read())  