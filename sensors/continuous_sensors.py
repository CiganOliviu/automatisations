import os
import time

number_of_iterations = 1000
iterator = 0


def apply_sensors_command():
    os.system('sensors')


def check_possibility_of_running_hddtemp(iterator : int) -> bool:

    contor = 5

    for item in range(1000):
        if item % 5 == 0:
            if iterator == item:
                return True

    return False


def apply_hddtemp_command(running_condition):
    if running_condition:
        os.system('sudo hddtemp /dev/sda')
        time.sleep(5)


def clear_system_screen():
    os.system('clear')


clear_system_screen()

while iterator < number_of_iterations:

    apply_sensors_command()
    running_condition = check_possibility_of_running_hddtemp(iterator)
    apply_hddtemp_command(running_condition)

    iterator += 1
    time.sleep(3)

    clear_system_screen()
