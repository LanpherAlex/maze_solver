import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells),num_cols,)
        self.assertEqual(len(m1._Maze__cells[0]),num_rows,)

    def test_maze_different_size(self):
        num_cols = 5
        num_rows = 7
        m2 = Maze(10, 10, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m2._Maze__cells), num_cols)
        self.assertEqual(len(m2._Maze__cells[0]), num_rows)

    def test_maze_square(self):
        num_cols = 8
        num_rows = 8
        m3 = Maze(5, 5, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m3._Maze__cells), num_cols)
        self.assertEqual(len(m3._Maze__cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        m4 = Maze(0, 0, 3, 3, 10, 10)  
        entrance = m4._Maze__cells[0][0]
        exit_cell = m4._Maze__cells[2][2]

        self.assertFalse(entrance.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_manual_visit_and_reset(self):
        m = Maze(0, 0, 2, 2, 10, 10, seed=0)
        m._Maze__cells[0][0].visited = True
        m._Maze__reset_cells_visited()
        self.assertFalse(m._Maze__cells[0][0].visited)

    def test_reset_cells_visited(self):
        m = Maze(0, 0, 2, 2, 10, 10, seed=0)
    
        # Manually mark some cells as visited
        m._Maze__cells[0][0].visited = True
        m._Maze__cells[1][0].visited = True
    
        m._Maze__reset_cells_visited()
    
        for i in range(2):
            for j in range(2):
                self.assertFalse(m._Maze__cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
