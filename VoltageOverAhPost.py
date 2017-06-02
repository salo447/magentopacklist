import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd

###       INPUTS        ###
input_csv = '25R.csv'     #Name of input CSV

colIndices = ['25R']   #Name of each column prefix
names = ['25R5']     #Line names for legend

var_of_interest = ['Volts']   #Choose y axis field from axis name
title = '25R5 20A DISCHARGE TEST'  #Graph title
x_axis_label = 'VOLTAGE'      #X axis label
y_axis_label = 'CAPACITY (mAh)'  #Y axis label
line_width = 3                #Graph line width

x_range = [0,2500,500]        #X axis range
y_range = [2.8,3.7,.2]			#Y axis range
###                     ###



###       SETUP         ###
#Set font properties for 
prop = font_manager.FontProperties(fname='C:\Roboto-Light.ttf', size=14)     #Xlabel, ylabel, and legend fonts
labelprop = font_manager.FontProperties(fname='C:\Roboto-Medium.ttf', size=12)  #Tick fonts
titleprop = font_manager.FontProperties(fname='C:\Roboto-Medium.ttf', size=20)  #Title fonts

df = pd.read_csv(input_csv, delimiter = ',', encoding="utf-8-sig")
colList = list(df.columns.values)

mydpi = 100
plt.figure(figsize=(1000/mydpi,800/mydpi), dpi=mydpi)
counter=0
###                     ###



###       PLOT          ###
for rank, column in enumerate(var_of_interest):
	# for index, batteryType in enumerate(colIndices):
     #    print(1+1)
     #    with plt.style.context('fivethirtyeight'):
     #    # with plt.style.context('fivethirtyeight'):
     #        plt.plot(df[batteryType+'Capacity'].values*1000,
     #            df[batteryType+column.replace("\n", " ")].values,
     #            lw=line_width, label=names[counter])
     #        counter+=1


    batteryType = '25R'
    with plt.style.context('fivethirtyeight'):
   # with plt.style.context('fivethirtyeight'):
       plt.plot(df[batteryType+'Capacity'].values,
           df[batteryType+column.replace("\n", " ")].values/1000,
           lw=line_width, label=names[counter])
       counter+=1

legend = plt.legend(loc='upper right', shadow=False)

for label in legend.get_texts():
    label.set_fontproperties(prop)

plt.title(title, fontproperties=titleprop, y=1.05)

axes = plt.gca()
axes.set_xlim([x_range[0],x_range[1]])
axes.set_ylim([y_range[0],y_range[1]])

for label in axes.get_xticklabels():
    label.set_fontproperties(labelprop)

for label in axes.get_yticklabels():
    label.set_fontproperties(labelprop)

plt.ylabel(x_axis_label, fontproperties=prop, labelpad=20)
plt.xlabel(y_axis_label, fontproperties=prop, labelpad=20)

plt.tight_layout(pad=1.3)
###                             ###



###        OUTPUT               ###
plt.savefig("VoltageOverAhPost.png", facecolor='#F0F0F0')
# plt.show()
###                             ###

