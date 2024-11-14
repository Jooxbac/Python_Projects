import os
# Clean screen command depending on the OS
os.system('cls' if os.name == 'nt' else 'clear')


class Board():
    def __init__(self):
        self.cells = ["O", "X", "O", " ", " ", " ", " ", " ", " ",]  # 9 cells

    def display(self):
        print(" %s | %s | %s " % (self.cells[0], self.cells[1], self.cells[2]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[3], self.cells[4], self.cells[5]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[6], self.cells[7], self.cells[8]))


board = Board()
board.display()

# Next lesson: https://www.youtube.com/watch?v=H1zsp0jTd5M&list=PLlEgNdBJEO-m6o4INllCF1FRMS262A5C_&index=2