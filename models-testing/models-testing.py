import pandas as pd
import numpy as np
import os
import csv

curr_dir = os.path.dirname(__file__)
output_dir = os.path.join(curr_dir, '..', '..', '..', 'Matlab/Edge/')

means_arr = np.load(curr_dir + "/npy/means.npy")
stds_arr = np.load(curr_dir + "/npy/stds.npy")

# file = open(output_dir + "norm_predicted_drop_rate.csv", "r")
file = open(output_dir + "outputs/model2/norm_predicted_drop_rate.csv", "r")
csv_reader = csv.reader(file)
pred_list = []
i = 0
for row in csv_reader:
    if i > 0:
        pred_list.append([])
        for val in row:
            pred_list[-1].append(float(val))
    i += 1

for row in range(len(pred_list)):
    mega_col = 27
    for col in range(len(pred_list[row])):
        pred_list[row][col] = (pred_list[row][col] * stds_arr[mega_col] + means_arr[mega_col])-1
        mega_col += 2
pred_df = pd.DataFrame(pred_list)

# file = open(output_dir + "actual_drop_rate.csv", "r")
file = open(output_dir + "outputs/model2/actual_drop_rate.csv", "r")
csv_reader = csv.reader(file)
actual_list = []
i = 0
for row in csv_reader:
    if i > 0:
        actual_list.append([])
        for val in row:
            actual_list[-1].append(float(val))
    i += 1
actual_df = pd.DataFrame(actual_list)

pred_output = output_dir + 'unnormalized/pred2.csv'
pred_df.to_csv(pred_output, mode = 'w', header = True, index = False)
actual_output = output_dir + 'unnormalized/actual2.csv'
actual_df.to_csv(actual_output, mode = 'w', header = True, index = False)



'''
li1 = [[1, 2], [3, 4]]
li2 = [100, 112]
li3 = [1000, 2000]

li = np.column_stack((li1, li2, li3))
print(li)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([100, 112])
arr3 = np.array([])

arr3 = np.column_stack((arr3, arr1, arr2))
print(arr3)

arr3 = np.array([1000, 2000])

arr = np.column_stack((arr1, arr2, arr3))
print(arr)

arr = np.row_stack((arr1, arr2, arr3))
print(arr)

test_list = [[1, 2, 3]]
df = pd.DataFrame(test_list)
df.loc[len(df)] = [10, 11, 12]
print(df)
'''