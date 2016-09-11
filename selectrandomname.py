import random
# see number of names in file
# num_names = sum(1 for line in open('hacknames.txt'))
# print num_names

random_name = random.choice(open('hacknames.txt').readlines())
print random_name
