from player import Player


class RandomAi(Player):
    pass


def main():
    ai = RandomAi('James')
    print(ai.get_name())


if __name__ == "__main__":
    main()
