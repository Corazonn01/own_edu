def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:  # Compare lengths
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

with open('input.txt', 'r') as file:
    line = file.readline().strip()
    words = [(word.strip("'"), len(word.strip("'"))) for word in line.strip("[]").split(', ')]

bubbleSort(words)

words_dict = {word[0]: word[1] for word in words}

with open('output.txt', 'w') as file:
    for word, length in words_dict.items():
        file.write(f'{word}: {length}\n')

print("Результаты записаны в файл output.txt.")
