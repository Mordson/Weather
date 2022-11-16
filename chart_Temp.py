import matplotlib.pyplot as plt #Importing matplotlib
import GetData as GD #Importing GetData.py

# create data
Date= GD.TableDate #Date
Temperature = GD.TableTemperature #Temperature

figure = plt.figure() #Creating figure
plt.axes = figure.add_subplot(1,1,1) #Creating axes

plt.axes.bar(
    range(len(Date)),
    Temperature,
    tick_label = Date
) #Creating bar chart

plt.xlabel("Date") #X label
plt.ylabel("Temperature in C") #Y label
plt.title("Temperature in C") #Title

plt.show() #Showing chart