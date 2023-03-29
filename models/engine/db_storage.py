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
        """_summary_

        Args:
            player_data (_type_): _description_

        Returns:
            _type_: _description_
        """
        player = models.Player(
            name=player_data['name'], age=player_data['age'], team_id=player_data['team_id'])
        self.data_base.add(player)
        self.data_base.commit()
        self.data_base.refresh(player)
        return player

    def create_coach(self, coach_data):
        """_summary_
        Args:
            coach_data (_type_): _description_
        Returns:
            _type_: _description_
        """
        coach = models.Coach(
            name=coach_data['name'], age=coach_data['age'], team_id=coach_data['team_id'])
        self.data_base.add(coach)
        self.data_base.commit()
        self.data_base.refresh(coach)
        return coach

    def create_team(self, team_data):
        """_summary_
        Args:
            team_data (_type_): _description_
        Returns:
            _type_: _description_
        """
        team = models.Team(name=team_data['name'], city=team_data['city'])
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
        return self.data_base.query(models.Player).filter(models.Player.id == player_id).first()

    def get_coach(self, coach_id):
        """_summary_
        Args:
            coach_id (_type_): _description_
        Returns:
            _type_: _description_
        """
        return self.data_base.query(models.Coach).filter(models.Coach.id == coach_id).first()

    def get_team(self, team_id):
        """_summary_
        Args:
            team_id (_type_): _description_
        Returns:
            _type_: _description_
        """
        return self.data_base.query(models.Team).filter(models.Team.id == team_id).first()
