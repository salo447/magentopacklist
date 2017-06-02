import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd

path = 'C:\Roboto-Light.ttf'
prop = font_manager.FontProperties(fname=path, size=14)
labelprop = font_manager.FontProperties(fname='C:\Roboto-Medium.ttf', size=12)
titleprop = font_manager.FontProperties(fname='C:\Roboto-Medium.ttf', size=20)

mydpi = 100

df = pd.read_csv('BatteryTest10A.csv', delimiter = ',', encoding="utf-8-sig")
colList = list(df.columns.values)
colIndices = ['1-10A', '2-10A']

x_range = [2.5,3.5,.2]   #midpoint = x_range[1] / 2
y_range = [20,50,10]

var_of_interest = ['Temp']
title = '10A DISCHARGE TEST'

plt.figure(figsize=(1000/mydpi,800/mydpi), dpi=mydpi)
for rank, column in enumerate(var_of_interest):
    # Plot each line separately with its own color, using the Tableau 20
    # color set in order.

    for index, batteryType in enumerate(colIndices):
        with plt.style.context('fivethirtyeight'):

            plt.plot(df[batteryType+'Volts'].values,
                df[batteryType+column.replace("\n", " ")].values,
                lw=3, label='CELL #'+batteryType[0])


legend = plt.legend(loc='upper right', shadow=False)

for label in legend.get_texts():
    label.set_fontproperties(prop)

plt.title(title, fontproperties=titleprop, y=1.05)


axes = plt.gca()
axes.set_xlim([x_range[0],x_range[1]])
axes.set_ylim([y_range[0],y_range[1]])

for label in axes.get_xticklabels() :
    label.set_fontproperties(labelprop)

for label in axes.get_yticklabels() :
    label.set_fontproperties(labelprop)

plt.ylabel('TEMPERATURE', fontproperties=prop, labelpad=20)
plt.xlabel('VOLTAGE', fontproperties=prop, labelpad=20)

plt.tight_layout(pad=1.3)



plt.savefig("VoltageOverAh.png", facecolor='#F0F0F0')
# plt.show()

