# Growtopia Current World
An application written in Python to write your current world in Growtopia to a text file.

## Motivation
To aid Growtopia streamers in displaying their current world to their viewers.

## Features
- Writes your current world in Growtopia to a text file every 5 seconds

## Code Example
```python
f = open(os.path.join(PATH, 'save.dat'), 'rb') # Open the save.dat file in byte format
f = open(os.path.join(PATH, 'current_world.txt'), 'w') # Write the current world to current_world.txt
```
