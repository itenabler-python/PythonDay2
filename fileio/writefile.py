
hellofile = open("helloworld.txt", "w")
hellofile.write("This is my 2nd hello world sentence ")
hellofile.close()

hellofile = open("helloworld.txt", "a")
hellofile.write("\nThis is my 3rd hello world sentence ")
hellofile.close()

