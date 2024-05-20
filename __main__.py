from src.game import Game


def main():
    """Creates instance of the Game and executes it."""
    game: Game = Game()
    game.run()


if __name__ == "__main__":
    main()
