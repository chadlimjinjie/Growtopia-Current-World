# Growtopia Current World
An application written in Python to write your current world in Growtopia to a text file.
## Table of contents
- [Motivation](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/README.md#motivation)
- [Features](https://github.com/chadlimjinjie/Growtopia-Current-World/blob/main/README.md#features)
- [Code Example]()
## Motivation
To aid Growtopia streamers in displaying their current world to their viewers.

## Features
- Writes your current world in Growtopia to a text file every 5 seconds

## Code Example

```python
f = open(os.path.join(PATH, 'current_world.txt'), 'w') # Write the current world to current_world.txt
time.sleep(5) # Update rate in second(s)
```
