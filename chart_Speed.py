import matplotlib.pyplot as plt
import GetData as GD

# create data
Date= GD.TableDate
Speed = GD.TableSpeed #Speed of wind

figure = plt.figure() #Creating figure
plt.axes = figure.add_subplot(1,1,1) #Creating axes

plt.axes.bar(
    range(len(Date)),
    Speed,
    tick_label = Date
) #Creating bar chart

plt.xlabel("Date") #X label
plt.ylabel("Speed in m/s") #Y label

plt.show() #Showing chart