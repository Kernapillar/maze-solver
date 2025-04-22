import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 2
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells2(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells3(self): 
        num_cols = 1
        num_rows = 14
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells), 
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    def test_maze_create_cells4(self): 
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells), 
            1
        )
        self.assertEqual(
            len(m1._cells[0]),
            1
        )
    
    def test_possible_neighbors(self): 
        m = Maze(0, 0, 2, 2, 10, 10, test=True)
        neighbors = m.possible_neighbors(0, 0, test=True) 
        print(neighbors)
        self.assertEqual(len(neighbors), 2)



if __name__ == "__main__":
    unittest.main()