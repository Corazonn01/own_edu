
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if len(arr[j][0]) > len(arr[j + 1][0]): 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

with open('input.txt', 'r') as file:
    line = file.readline().strip()
    words = [(word.strip("'"), len(word.strip("'"))) for word in line.strip("[]").split(', ')]  

bubbleSort(words)

print("That is a sorted array:")
for word, length in words:
    print(f"{word}: {length}")
