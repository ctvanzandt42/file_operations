from sys import argv
import os 

script, filename = argv
print("""
In {}, I'm going to create a file named {}, write whatever you'd like to it, and run it.
The file will have a maximum of three lines. 
Ready to get started?""".format(script, filename))

target = open(filename, "w+")
line1 = input("Write the first line here: ")
line2 = input("Write the second line here: ")
line3 = input("Write the third line here: ")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))
target.close()

print("Now running the file\n\n")

readable = open(filename)

if filename.endswith('.py'): 
    os.system(f"sudo python3 {filename}")
elif filename.endswith('.js'):
    os.system(f"sudo node {filename}")
else:
    print(readable.read())

readable.close()
os.remove(filename)




