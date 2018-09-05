from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import csv

##### Processing Cards #####
# Break data into lists
with open("./data.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content = [x.split(", ") for x in content] 

# For each list, calculate pair wise frequency
for i in range(len(content)):
	for j in range(len(content[i])):
		content[i][j] = int(content[i][j]) 

final_list = []
for row_index in range(64):
    for col_index in range(64):
        counter_a = 0
    	for l in content:
            if (row_index+1) in l and (col_index+1) in l and (row_index+1) != (col_index+1):
                counter_a = counter_a + 1
        print "row: " + str(row_index) + " col: " + str(col_index) + " val: " + str(counter_a)
        final_list.append(counter_a)

final_list = [final_list[i:i+64] for i in xrange(0, len(final_list), 64)]
for r in range(64):
    for c in range(64):
        if r == c:
            continue 
        else:
            final_list[r][c] = 13 - (final_list[r][c])

print final_list
# Present Matrix
for row in final_list:
    for item in row:
        print item,
    print

# Write to a CSV file
with open("./data.csv", "w") as output:
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerows(final_list)

# Generate the final dendrograms
mat = np.array(final_list)
linkage_matrix = linkage(mat, "single") # Configure Linkage Method
dendrogram(linkage_matrix, color_threshold = 38)
plt.title("Item-by-item")
plt.show()
