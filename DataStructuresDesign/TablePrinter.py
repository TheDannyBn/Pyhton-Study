def printTable(tableData):
    # Determine the number of columns (i.e., number of inner lists)
    num_cols = len(tableData)
    num_rows = len(tableData[0])

    # Create a list to hold the maximum width of each column
    colWidths = [0] * num_cols

    # Compute the maximum string length for each column
    for i in range(num_cols):
        colWidths[i] = max(len(item) for item in tableData[i])

    # Print the table row by row
    for row in range(num_rows):
        row_items = []
        for col in range(num_cols):
            # Right-justify each string using the corresponding column width
            row_items.append(tableData[col][row].rjust(colWidths[col]))
        print(' '.join(row_items))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
