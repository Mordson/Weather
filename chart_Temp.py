import matplotlib.pyplot as plt
import GetData as GD

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

plt.show() #Showing chart