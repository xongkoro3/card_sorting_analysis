# Calculating Average Rank #
import sys
import operator
from rank_low_inc import get_sorted_card_list

# return type: (index, rank)
def safe_div(x,y):
    if y == 0:
        return 0
    return x / y


def find_in_list_of_list(mylist, n):
	tList = []
	for sub_list in mylist:
		if n in sub_list:
			tList.append([mylist.index(sub_list), sub_list.index(n)+1])
			continue
	return tList

def compute_cluster_avg_rank(ordered_list, cards):
	cluster = []
	for c in cards:
		c_rank = ordered_list[c-1][1]
		cluster.append(c_rank)
	cluster_avg_rank = safe_div(sum(cluster),len(cluster))
	return cluster_avg_rank

def break_into_array(sourceFile):
	with open(sourceFile) as f:
		allP = []
		p = []
		for line in f:
			p += line.strip().split(", ")
			if line in ['\n', '\r\n']:
				allP.append(p[:-1])
				p = []
				continue

	for i in range(len(allP)):
		for j in range(len(allP[i])):
			allP[i][j] = int(allP[i][j]) 
	
	# Get the number of cards used by each participant
	for i in allP:
		print len(i)
	return allP
	
l = break_into_array("./high_inc.txt")
print l
print "this is " + str(len(l))

# Compute rank
sorted_list = []
for i in range(1, 65):
	a = find_in_list_of_list(l, i)
	rank = [item[1] for item in a]
	if len(rank) < len(l) and len(rank) != 0:
		add_on = [64] * (len(l) - len(rank))
		rank.extend(add_on)
	avg_rank = safe_div(sum(rank),len(rank))
	sorted_list.append([i, avg_rank])

# Ordered cards with rank


# sorted_list = sorted(sorted_list, key=operator.itemgetter(1))
# print "\n"
# print sorted_list

# Cards 
with open("cards.txt") as f:
    cards = f.readlines()

# print cards
card_with_rank = []
for card in cards:
	card_index = cards.index(card)
	c = [card]
	c.append(sorted_list[card_index][1])
	card_with_rank.append(c)

# Sort the cards based on rank
sorted_card_with_rank = sorted(card_with_rank, key=operator.itemgetter(1))

# Remove card #48
sorted_card_with_rank.pop(0)

print sorted_card_with_rank

# Write final sorted result to file
final_file = open('test_high_inc.txt', 'w')
for item in sorted_card_with_rank:
	final_file.write("%s" % item[0])

# Clusters
blue = [54, 16, 63, 61, 23, 2, 22]
blue_rank = compute_cluster_avg_rank(sorted_list, blue)

green = [35, 28, 31, 40, 33, 39, 50, 51, 18, 19, 46, 34, 9, 36, 37, 41, 47]
green_rank = compute_cluster_avg_rank(sorted_list, green)

pink = [24, 26, 30, 17, 32]
pink_rank = compute_cluster_avg_rank(sorted_list, pink)

red = [8, 29, 60, 7, 43, 44, 48, 53, 58, 11, 6, 56, 1, 5, 25, 21, 12, 57]
red_rank = compute_cluster_avg_rank(sorted_list, red)

yellow = [10, 15, 42, 52, 38, 49, 3, 55, 13, 59, 4, 20, 64, 14, 27, 45, 62]
yellow_rank = compute_cluster_avg_rank(sorted_list, yellow)

print "Blue: " + str(blue_rank) + ", Green: " + str(green_rank) + ", Pink: " + str(pink_rank) + ", Red: " + str(red_rank) + ", Yellow: " + str(yellow_rank)


# a = compute_cluster_avg_rank(sorted_list, [54, 16, 63])
# b = compute_cluster_avg_rank(sorted_list, [61, 23, 2, 22])

# print "brand: " + str(a) + ", cost related subcluster: " + str(b)

# test = compute_cluster_avg_rank(sorted_list, [50, 51, 18, 19, 46, 34, 9, 36, 37, 41, 47])
# print test

# test = compute_cluster_avg_rank(sorted_list, [34, 9, 36])
# print test

# test = compute_cluster_avg_rank(sorted_list, [37, 41, 47])
# print test


test = compute_cluster_avg_rank(sorted_list, [1, 5, 25, 21, 12, 57])
print test

# test = compute_cluster_avg_rank(sorted_list, [1, 5, 25, 21, 12, 57])
# print test

# Calculate difference

s_high = sorted_list
s_low = get_sorted_card_list() #from rank_low_inc
s_diff = []
for sub_list in s_high:
	list_low_idx = sub_list[0]-1
	s_diff.append([sub_list[0], cards[list_low_idx], sub_list[1] - s_low[list_low_idx][1], sub_list[1], s_low[list_low_idx][1]])

sorted_card_with_diff = sorted(s_diff, key=operator.itemgetter(2))
print "this is s_diff \n", sorted_card_with_diff

diff_file = open('test_diff.txt', 'w')
for i in sorted_card_with_diff:
	diff_file.write("%s" % i[1])
