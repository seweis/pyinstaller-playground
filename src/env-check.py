import sys
import os

print(sys.executable)
print(os.popen('python --version').read())


with open('my_new_file.txt', 'w') as file:
	file.write('This is a new file!')

input('Say something!')