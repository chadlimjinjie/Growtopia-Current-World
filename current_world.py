import os
import time

USER = os.environ['USERPROFILE']
PATH = os.path.join(USER, 'AppData/Local/Growtopia')

while True:
    f = open(os.path.join(PATH, 'save.dat'), 'rb') # Open the save.dat file in byte format
    text = str(f.read()) # Read the text
    text = text.split('lastworld')[1].split('tankid_checkbox')[0]
    text = text.replace('\\', '')
    text = text.replace('x05x00x00x00x0fx00x00x00', '')
    text = text.split('x00')[3]
    current_world = 'Current world: {}'.format(text.upper())
    f.close()
    f = open(os.path.join(PATH, 'current_world.txt'), 'w')
    f.write(current_world)
    f.close()
    time.sleep(5)