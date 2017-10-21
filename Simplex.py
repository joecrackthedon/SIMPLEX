# Simplex Method
# October 20, 2017

# This program utilizes simplex method to optimize a linear program
# The program accepts an augmented matrix in tableau form
# The input most be a list, and the first three inputs indicate:
# Number of rows, columns, 'max' or 'min'

# Example Formatting a 3 Rows x 4 Columns Tableau
# input = [ numofrows, numofcolumns,
#           valueR1C1, valueR1C2, valueR1C3, valueR1C4
#           valueR2C1, valueR2C2, valueR2C3, valueR2C4
#           valueR3C1, valueR3C2, valueR3C3, valueR3C4]

# The 3rd item in list should be a string: either 'min' or 'max'
# The first column values represent the minimazing or maximazing coefficients.
# The last column represents the RHS of the equations in standard form. 

example = [ 3,6,'max',
               1,-1,-1,0,0,0,
               0, 2, 1,1,0,4,
               0, 1, 2,0,1,3  ]


def extract_matrix(user_input):
    del user_input[0]
    del user_input[0]
    del user_input[0]
    return user_input


#def simplex(user_input):
    # Identify basic variables



def restrictions(columns):
    print('The program has detected',(columns-1),'variables\n',
          'Please identify restrictions'


def main(matrix):

    # Extracting Matrix Information
    rows = matrix[0]
    columns = matrix[1]
    optm_type = matrix[2]

    # Removing conditional inputs
    matrix = extract_matrix(matrix)

    

    

main(example)
