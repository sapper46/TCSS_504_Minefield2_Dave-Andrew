import random

def generate_minefield(rows, cols, mine_percentage):
    minefield = [['.' for _ in range(cols)] for _ in range(rows)]
    total_cells = rows * cols
    num_mines = int(total_cells * (mine_percentage / 100))

    for _ in range(num_mines):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        minefield[row][col] = '*'

    return minefield

def write_minefield_to_file(rows, cols, minefield, filename):
    with open(filename, 'a') as file:
        file.write(f"{rows} {cols}\n")
        for x in range(rows):
            for y in range(cols):
                file.write(minefield[x][y])
            file.write('\n')
        file.write('\n')


def main():
    while True:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        mine_percentage = float(input("Enter the percentage of mines (0-100): "))

        minefield = generate_minefield(rows, cols, mine_percentage)

        filename = 'minefield_data.txt'
        write_minefield_to_file(rows, cols, minefield, filename)

        another_minefield = input("Do you want to enter data for another minefield? (yes/no): ")
        if another_minefield.lower() != 'yes':
            break

if __name__ == "__main__":
    main()