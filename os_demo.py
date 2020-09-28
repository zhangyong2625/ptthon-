import os

path = os.getcwd()
print(path)
if not os.path.exists(path+"\\"+"result"):
    os.mkdir("result")
os.chdir(path+"\\"+"result")
with open("abc.txt", "w") as f:
    f.write("Python")
