
def read_input(file_path):
    """
    function to read input from a file
    """
    # open input file
    with open(file_path, 'r') as input_file:  # with open keeps us from having to explicitly close the file
        # create a list of input from file, removing white space and empty lines
        lines = [line.strip() for line in input_file if line.strip()]
    inputs, current_field = [], [] # variables for storin inputs and current field data
    # process minefield data, separating fields
    for line in lines:
        if ' ' in line:  # if space in line we know it's a minefield dimension
            if current_field:  # check if we're in a minefield
                inputs.append(current_field)  # add our current data to inputs list to save
                current_field = []  # reset current field to empty
            if line == "0 0":  # break on empty minefield
                break
        else: # add non-dimension lines to current field data
            current_field.append(line)
    if current_field:  # confirm no unsaved minefield data
        inputs.append(current_field)
    return inputs # return inputs

def count_mines(field, x, y):
    """
    counts mines around a specific cell
    """
    mine_count = 0
    for i in range(max(0, x - 1), min(len(field), x + 2)): # iterate over grid surrounding the cell
        for j in range(max(0, y - 1), min(len(field[i]), y + 2)):
            if field[i][j] == '*': # add a mine to the count if found
                mine_count += 1
    return mine_count # return mine count

def process_fields(inputs):
    """
     process each field and generate mine count
    """
    minefield = []
    for field_number, field in enumerate(inputs, 1): # enumerate over fields for field number and data
        output = f"Field #{field_number}:\n" # start generating output with field count
        for x, row in enumerate(field): # enumerate over each row and cell in the field
            for y, cell in enumerate(row):
                output += '*' if cell == '*' else str(count_mines(field, x, y)) # add * and mine count to output
            output += "\n"
        minefield.append(output.strip())
    return minefield # return processed fields


def generate_file(output_file, file_outputs):
    """
    adds generated oututs to the specified output file
    """
    output_file = open(output_file, 'w')
    num_outputs = len(file_outputs)
    for i, data in enumerate(file_outputs): # keep track of the index as we iterate over our output data
        output_file.write(data)
        if i < num_outputs - 1:
            output_file.write("\n\n")  # add two newlines for all but the last block
        else:
            output_file.write("\n")  # add only one newline for the last block
    output_file.close()


# file_path = 'mines_test_input.txt'
file_path = 'mines.txt'
output_path = 'minesweeper_output.txt'

inputs = read_input(file_path)

# Process the fields and generate output
outputs = process_fields(inputs)

generate_file(output_path, outputs)
