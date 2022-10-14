import matplotlib.pyplot as plt
import GetData as GD

# create data
Date= GD.TableDate
Temperature = GD.TableTemperature

figure = plt.figure()
plt.axes = figure.add_subplot(1,1,1)

plt.axes.bar(
    range(len(Date)),
    Temperature,
    tick_label = Date
)

plt.show()