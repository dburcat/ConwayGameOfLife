import unittest

from zipcodeconway.conway_game_of_life import ConwayGameOfLife


class ConwayGameOfLifeTest(unittest.TestCase):
    def test_run_test_1(self):
        start = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        sim = ConwayGameOfLife(5, start)
        results = sim.simulate(9)
        self.assertEqual(results, expected)

    def test_run_test_2(self):
        start = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        sim = ConwayGameOfLife(5, start)
        results = sim.simulate(10)
        self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()
