'''import matplotlib
print(matplotlib.__version__)'''
import matplotlib.pyplot as plt
import numpy as np

#xpoint=np.array([0,6])
#ypoint=np.array([0,250])

#plt.plot(xpoint,ypoint,'.')
#plt.show()

'''ypoint=np.array([0,250])

plt.plot(ypoint,color='red',linestyle='dotted')
plt.show()'''

#multiple data
'''x1=np.array([10,20,5,60])
y1=np.array([6,5,40,28])
x2=np.array([9,18,26,30])
y2=np.array([65,52,43,10])

plt.title("Sport Whatch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x1,y1,x2,y2)
plt.show()
'''
#scatter when there is a difference in values
'''x=np.array([10,20,5,60,50])
y=np.array([6,5,40,28,90])

plt.scatter(x,y)
plt.show()'''

#bar
'''x=np.array([10,20,5,60,50])
y=np.array([6,5,40,28,90])

plt.bar(x,y)
plt.show()'''

#histogram
'''x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()'''

#piechart
x=np.array([10,20,5,60,50])
mylables=["apple","B","C","D","E"]
plt.pie(x,labels=mylables)
plt.show()



