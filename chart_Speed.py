from turtle import speed
import matplotlib.pyplot as plt
import GetData as GD

# create data
Date= GD.TableDate
Speed = GD.TableSpeed

figure = plt.figure()
plt.axes = figure.add_subplot(1,1,1)

plt.axes.bar(
    range(len(Date)),
    Speed,
    tick_label = Date
)

plt.show()