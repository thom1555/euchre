from player import Player


class Team:
    def __init__(self, name: str, player_one: Player, player_two: Player):
        self.team_name = name
        self.p_1 = player_one
        self.p_2 = player_two
        self.points = 0

    def get_team_name(self):
        return self.team_name

    def get_points(self):
        return self.points

    def add_points(self, num):
        self.points += num
        # check for win

    def display_team(self):
        print("Team: " + self.get_team_name() + "!")


def main():
    p1 = Player('Billy')
    p2 = Player('Timmy')
    my_team = Team(p1, p2)
    my_team.display_team()


if __name__ == "__main__":
    main()
