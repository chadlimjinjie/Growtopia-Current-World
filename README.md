# Growtopia Current World
An application written in Python to write your current world in Growtopia to a text file.

![alt text](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/Screenshot%202020-10-04%20142916.png?raw=true)
## Table of contents
- [Motivation](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/README.md#motivation)
- [Features](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/README.md#features)
- [Code Example]()
- [Installation](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/README.md#installation)
- [How to use?]()
- [Contribute](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/README.md#contribute)
- [Credits](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/README.md#credits)
## Motivation
To aid Growtopia streamers in displaying their current world to their viewers.
## Features
- Writes your current world in Growtopia to a text file every 5 seconds interval
- More to come by community suggestions...
## Code Example
```python
USER = os.environ['USERPROFILE'] # e.g. C:/Users/chadl/
PATH = os.path.join(USER, 'AppData/Local/Growtopia/') # Growtopia download location
f = open(os.path.join(PATH, 'current_world.txt'), 'w') # Write the current world to current_world.txt
time.sleep(5) # Update rate in second(s)
```
## Installation

## How to use?
After building or downloading the .exe file open it and you're ready to go!
Use whatever streaming tool you are using and add a text to the streaming tool pointing to the current_world.txt file in the Growtopia folder.
## Contribute
Like my project? join my [Discord](https://discord.gg/G5EJHjz) channel! 
## Credits
Credits to users who back my project :)
