#! /bin/python3


import serial
import csv
import time


class Cignal_remote():
    commands = []

    ser = serial.Serial("/dev/ttyACM0", 9600)

    commands_file = open("/home/james/Desktop/Home_Automation/api/files/Cignal_remote.csv", "r")
    cursor = csv.DictReader(commands_file)

    for row in cursor:
        commands.append(row)

    
        
    def send_command(self, command_name): 
        for command in self.commands:
            if command["Command"] == command_name:
                current_command = command["Value"]

        self.ser.write(bytes(current_command, "ascii"))
        time.sleep(2)

        '''command_name = ["Back"]
        for x in range(len(command_name) + 1):
            for command in self.commands:
                if command["Command"] == command_name[x]:
                    current_command = command["Value"]

            self.ser.write(bytes(current_command, "ascii"))
            time.sleep(2)'''

    def send_channel_command(self, command_name):
        channels = {"discovery": ['1', '4', '0'], "nat_geo": ['1', '4', '1'], "fox_movies": ['5', '5']}
#        print(command_name)
        input_sequence = channels[command_name]
#        print(input_sequence)
        for command_input in input_sequence:
#            print("Command_input :" + command_input)
            for command in self.commands:
#                print("Command :" + str(command))
                if command["Command"] == command_input:
                    channel_command = command["Value"]
#                    print("Current command :" + channel_command)
                
            self.ser.write(bytes(channel_command, "ascii"))
            time.sleep(2)

#remote = Cignal_remote()
#remote.send_channel_command("nat_geo")
#send_command(commands, "Back")
#send_command(commands, "Volume_up")

#print("Sleeping")
#time.sleep(3)

#print("done")
