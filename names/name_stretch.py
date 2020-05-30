import time
from bst_stretch import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")
f.close()

duplicates = []
bst_return = BSTNode(names_1[0])

for name in names_1:
    bst_return.insert(name)

for name in names_2:
    if bst_return.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
