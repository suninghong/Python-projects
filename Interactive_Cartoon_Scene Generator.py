import csv

def get_words(line):
    segments = line.split('*') 
    return list(filter(None, segments))  # Throughout trials and errors,there is a need to filter out empty string.Searched on the internet

def check_puzzle(filename):
    
    with open("dictionary.txt", "r") as file:
        dictionary = file.read().split() 

    grid = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile) 
        for row in reader:
            grid.append(row)

    illegal_words = []

    # Bottom to down
    for row_index, row in enumerate(grid): # Search on google about the usage of enumerate
        row_string = ''.join(row)  # Join letters in one row into a single string, with string type
        words = get_words(row_string)  # Get non-empty segments from getword function
        for word in words: #For loop and if condition to check if the word is in the dictionary
            if word not in dictionary:
                illegal_words.append(f"across {row_index}: {word}")


    # Left to right
    for col_index in range(len(grid[0])):
        column_string = ''
        for row_index, row in enumerate(grid):  # Using enumerate for row iteration
            column_string += row[col_index]  # Build the vertical string of all characters in the column
        for word in get_words(column_string):
            if word not in dictionary:
                illegal_words.append(f"down {col_index}: {word}")



    return illegal_words

def main():
    puzzle_filename = "puzzle02.csv"
    answer = check_puzzle(puzzle_filename)
    print(answer)

if __name__ == "__main__":
    main()
