'''
For visualization/verification of selected pixels from vertices.txt, 
This code plots a scatter plot of the selected pixels from vertices path, 
and overlays it on top of an IR image from file path.
'''

import seaborn as sn, matplotlib.pyplot as plt, pandas as pd, numpy as np,sys
sys.path.insert(1,'/home/yehyun/TFPX/final-codes/utils')
from excelCoords import excelCoords

vPath = r"/home/yehyun/TFPX/final-codes/projects/IR-calibration/example/vertices.csv"
fPath = r"/home/yehyun/Downloads/CO2_test_March21_2024/Plaquette_NoHeater_flapped_03212024/03_21_24_11_03_17_IRImage.csv"

'''
vPath = input("Input vertices path: ")
fPath = input("Input file path: ")
'''

#graphs the heatmap
data = pd.read_csv(fPath).values.tolist()
npData = np.array(data)

hm = sn.heatmap(data = data, vmin = np.min(npData), vmax = np.max(npData), cmap = 'coolwarm')

#graphs the polygon points
data = excelCoords(vPath)
x_values = [point[1] for point in data]
y_values = [point[0] for point in data]

plt.scatter(x_values, y_values, color='yellow', marker = 'o', alpha = 0.05)

#sets the graph parameters
plt.title('Highlighted Pixels with Heatmap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
