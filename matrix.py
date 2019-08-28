class Matrix(object):
    def __init__(self, matrix_string):
      self.matrix_string=matrix_string.split('\n')
      global no_of_rows
      global no_of_columns
      no_of_rows=len(self.matrix_string)
      no_of_columns=len(self.matrix_string[0])
      n=1  
      global list_of_rows
      list_of_rows=[]
      for string in self.matrix_string: 
         string_split=string.split()
         items_in_row=[]
         for char in string_split:
            if char==' ':
               pass
            else:
               items_in_row.append(int(char))
         n=n+1
         list_of_rows.append(items_in_row)

    def row(self, index):
      return list_of_rows[index-1]
    def column(self, index):
        n=0
        list_of_column=[]
        while n<no_of_rows:
            list_of_column.append(list_of_rows[n][index-1])
            n+=1
        return list_of_column
##################################################################################################################
#Given a string representing a matrix of numbers, return the rows and columns of that matrix.
#
#So given a string with embedded newlines like:
#
#9 8 7
#5 3 2
#6 6 7
#
#representing this matrix:
#
#    1  2  3
#  |---------
#1 | 9  8  7
#2 | 5  3  2
#3 | 6  6  7
#
#your code should be able to spit out:
#
#    A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
#    A list of the columns, reading each column top-to-bottom while moving from left-to-right.
#
#The rows for our example matrix:
#
#    9, 8, 7
#    5, 3, 2
#    6, 6, 7
#
#And its columns:
#
#    9, 5, 6
#    8, 3, 6
#    7, 2, 7
#
##############################################################################################################
