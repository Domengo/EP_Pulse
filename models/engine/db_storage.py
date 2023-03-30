"""
It's importing the classes that we're going to use in this file.
"""
from sqlalchemy.orm import Session
from models.player import Player
from models.coach import Coach
from models.team import Team


class DataStorage:
    """_summary_
    """

    def __init__(self, data_base: Session):
        self.data_base = data_base

    def create_player(self, player_data):
        """
        _summary_
        
        Here's a longer description of the function: _description_
        
        :param player_data: {'name': 'John', 'age': '20', 'team_id': '1'}
        :return: A player object
        """
        player = Player(
            name=player_data['name'], age=player_data['age'], team_id=player_data['team_id'])
        self.data_base.add(player)
        self.data_base.commit()
        self.data_base.refresh(player)
        return player

    def create_coach(self, coach_data):
        """
        _summary_
        
        :param coach_data: This is the data that we're going to use to create a new coach
        :return: The coach object
        """
        coach = Coach(
            name=coach_data['name'], age=coach_data['age'], team_id=coach_data['team_id'])
        self.data_base.add(coach)
        self.data_base.commit()
        self.data_base.refresh(coach)
        return coach

    def create_team(self, team_data):
        """
        _summary_
        
        :param team_data: This is the data that is passed in from the request
        :return: The team object
        """
        team = Team(name=team_data['name'], city=team_data['city'])
        self.data_base.add(team)
        self.data_base.commit()
        self.data_base.refresh(team)
        return team

    def get_player(self, player_id):
        """_summary_
        Args:
            player_id (_type_): _description_
        Returns:
            _type_: _description_
        """
        return self.data_base.query(Player).filter(Player.id == player_id).first()


    def get_coach(self, coach_id):
        """
        _summary_
        > Get the coach with the given id from the database

        :param coach_id: the id of the coach
        :return: A list of all the coaches in the database.
        """
        return self.data_base.query(Coach).filter(Coach.id == coach_id).first()

    def get_team(self, team_id):
        """
        _summary_
        
        :param team_id: The id of the team you want to get
        :return: The first team in the database with the id of team_id.
        """
        return self.data_base.query(Team).filter(Team.id == team_id).first()
