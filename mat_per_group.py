from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import csv
import sys

##### Processing Cards #####
# Break data into lists
with open("./"+sys.argv[1]) as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content = [x.split(", ") for x in content] 

# For each list, calculate pair wise frequency
for i in range(len(content)):
	for j in range(len(content[i])):
		content[i][j] = int(content[i][j]) 

total_groups = len(content)

content_numbers = []
for i in content:
    content_numbers += i

for i in range(1,65):
    if i not in content_numbers:
        print i

final_list = []
for row_index in range(64):
    for col_index in range(64):
        counter_a = 0
    	for l in content:
            if (row_index+1) in l and (col_index+1) in l and (row_index+1) != (col_index+1):
                counter_a = counter_a + 1
        #print "row: " + str(row_index) + " col: " + str(col_index) + " val: " + str(counter_a)
        final_list.append(counter_a)

final_list = [final_list[i:i+64] for i in xrange(0, len(final_list), 64)]

for r in range(len(final_list)):
    for c in range(len(final_list)):
        if r == c:
            continue
        else:
            final_list[r][c] = total_groups - final_list[r][c] 

for row in final_list:
    for item in row:
        print item,
    print

mat = np.array(final_list)
linkage_matrix = linkage(mat, "single")
dendrogram(linkage_matrix)
plt.title("Item-by-item")
plt.show()
