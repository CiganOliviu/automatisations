import os
import time

number_of_iterations = 1000
iterator = 0

while iterator < number_of_iterations:

    os.system('sensors')
    iterator += 1
    time.sleep(2)
    os.system('clear')
