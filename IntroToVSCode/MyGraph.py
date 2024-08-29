import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0 ,20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hi there!")

#step one
#create your virtual enviornemnt 
# for macs:
#python3 -m venv myvenv(virtual enviornment)

#step two
#activate your VE
# for macs
#source myvenv/bin/activate

#stepthree
#install 3rd party libraries
# pip3 install matplotlib(virtual enviornment)
# make sure your on the right intepreter 

#Version control - project level
#Source control - development aspect of your application, the source code that makes your application works
#Use it to track our projects
        #each coder will clone a repository to check if each part of the code is right
        #each coder will do a pull request and project manager approve it and it becomes apart of the new website 