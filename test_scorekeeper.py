import unittest
from flask_testing import TestCase
from scorekeeper import app

class TestScorekeeper(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    # The test_player1_wins, test_player2_wins, and test_invalid_scores methods test the match_result endpoint with different scores.
    # test_player1_wins sends scores where player 1 wins (7-6, 2-6, 6-3).
    def test_player1_wins(self):
        response = self.client.post('/match_result', json={'scores': [[7, 6], [2, 6], [6, 3]]})
        self.assertEqual(response.json, {'result': 1})
    # test_player2_wins sends scores where player 2 wins (6-7, 6-2, 3-6).
    def test_player2_wins(self):
        response = self.client.post('/match_result', json={'scores': [[6, 7], [6, 2], [3, 6]]})
        self.assertEqual(response.json, {'result': 2})
    # test_invalid_scores sends scores where player 1 and player 2 win the same number of games (6-6, 6-6, 6-6).
    def test_invalid_scores(self):
        response = self.client.post('/match_result', json={'scores': [[6, 6], [6, 6], [6, 6]]})
        self.assertEqual(response.json, {'error': 'Invalid scores'})

if __name__ == '__main__':
    unittest.main()