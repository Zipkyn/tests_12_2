import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.all_results = {}

    def setUp(self):

        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):

        for test_name, results in cls.all_results.items():
            print(f"{test_name}: {', '.join([f'{place}: {runner}' for place, runner in results.items()])}")

    def test_usain_nick(self):

        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results["usain_nick"] = results
        self.assertTrue(results[max(results.keys())] == self.nick)

    def test_andrei_nick(self):

        tournament = Tournament(90, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results["andrei_nick"] = results
        self.assertTrue(results[max(results.keys())] == self.nick)

    def test_usain_andrei_nick(self):
        
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results["usain_andrei_nick"] = results
        self.assertTrue(results[max(results.keys())] == self.nick)

if __name__ == "__main__":
    unittest.main()

