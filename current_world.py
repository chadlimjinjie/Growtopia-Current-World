'''
Author: Chad Lim Jin Jie
Title: Growtopia Current World
GitHub: https://github.com/chadlimjinjie/
'''
import os
import time

USER = os.environ['USERPROFILE'] # e.g. C:/Users/chadl/
PATH = os.path.join(USER, 'AppData/Local/Growtopia/') # Growtopia download location

print('Developed by Chad Lim Jin Jie')
print('GitHub: https://github.com/chadlimjinjie/')

while True:
    has_file = False
    try:
        f = open(os.path.join(PATH, 'save.dat'), 'rb') # Open the save.dat file in byte format
        has_file = True
    except FileNotFoundError as e:
        pass
    if has_file:
        text = str(f.read()) # Read the text in the save.dat file
        text = text.split('lastworld')[1].split('tankid_checkbox')[0]
        text = text.replace('\\', '')
        text = text.replace('x05x00x00x00x0fx00x00x00', '')
        text = text.split('x00')[3].split('x05')[0]
        current_world = 'Current world: {}'.format(text.upper())
        f.close()
        f = open(os.path.join(PATH, 'current_world.txt'), 'w') # Write to current_world.txt
        f.write(current_world)
        f.close()
        print(current_world)
        time.sleep(5) # Update rate in second(s)
    else:
        break
