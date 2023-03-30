"""
It creates a database connection, creates an instance of the DataStorage class, creates a player,
# coach, and team, and then tests the relationships between the objects.
"""
import unittest
from sqlalchemy.orm import Session
from models.base_model import Base
from models.engine.db_storage import DataStorage


class TestDataStorage(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.db = Session(bind='sqlite:///:memory:')
        Base.metadata.create_all(self.db.bind)

        # Create an instance of the DataStorage class for testing
        self.storage = DataStorage(self.db)

    def tearDown(self):
        """
            It creates a database connection, and then closes it when the test is done
        """
        self.db.close()

    def test_create_player(self):
        """
        It creates a player.
        """
        player_data = {'name': 'John Doe', 'age': 25, 'team_id': 1}
        player = self.storage.create_player(player_data)

        self.assertEqual(player.name, player_data['name'])
        self.assertEqual(player.age, player_data['age'])
        self.assertEqual(player.team_id, player_data['team_id'])

    def test_create_coach(self):
        """
        It creates a coach object and assigns it to the variable coach.
        """
        coach_data = {'name': 'Jane Smith', 'age': 35, 'team_id': 1}
        coach = self.storage.create_coach(coach_data)

        self.assertEqual(coach.name, coach_data['name'])
        self.assertEqual(coach.age, coach_data['age'])
        self.assertEqual(coach.team_id, coach_data['team_id'])

    def test_create_team(self):
        """
        It creates a team.
        """
        team_data = {'name': 'Example Team', 'city': 'New York'}
        team = self.storage.create_team(team_data)

        self.assertEqual(team.name, team_data['name'])
        self.assertEqual(team.city, team_data['city'])

    def test_get_player(self):
        """
        It creates a player and then retrieves the player.
        """
        player_data = {'name': 'John Doe', 'age': 25, 'team_id': 1}
        player = self.storage.create_player(player_data)

        retrieved_player = self.storage.get_player(player.id)

        self.assertEqual(retrieved_player.name, player_data['name'])
        self.assertEqual(retrieved_player.age, player_data['age'])
        self.assertEqual(retrieved_player.team_id, player_data['team_id'])

    def test_get_coach(self):
        """
        It creates a coach and then retrieves the coach.
        """
        coach_data = {'name': 'Jane Smith', 'age': 35, 'team_id': 1}
        coach = self.storage.create_coach(coach_data)

        retrieved_coach = self.storage.get_coach(coach.id)

        self.assertEqual(retrieved_coach.name, coach_data['name'])
        self.assertEqual(retrieved_coach.age, coach_data['age'])
        self.assertEqual(retrieved_coach.team_id, coach_data['team_id'])

    def test_get_team(self):
        """
        It creates a team, then retrieves it and asserts that the retrieved team has the same name and city
        as the team that was created.
        """
        team_data = {'name': 'Example Team', 'city': 'New York'}
        team = self.storage.create_team(team_data)

        retrieved_team = self.storage.get_team(team.id)

        self.assertEqual(retrieved_team.name, team_data['name'])
        self.assertEqual(retrieved_team.city, team_data['city'])

    def test_relationships(self):
        """
        The function tests the relationships between the objects.
        """
        team_data = {'name': 'Example Team', 'city': 'New York'}
        team = self.storage.create_team(team_data)

        coach_data = {'name': 'Jane Smith', 'age': 35, 'team_id': team.id}
        coach = self.storage.create_coach(coach_data)

        player_data = {'name': 'John Doe', 'age': 25, 'team_id': team.id}
        player = self.storage.create_player(player_data)

        # Test the relationships between the objects
        self.assertEqual(team.players[0], player)
        self.assertEqual(team.coach, coach)
        self.assertEqual(player.team, team)


if __name__ == "__main__":
    unittest.main()
