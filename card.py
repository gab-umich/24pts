class Card:
    """Card with only rank value, no suit"""
    rank = 0

    def __init__(self, rank):
        """

        :type rank: int or char
        """
        if rank == 'A':
            self.rank = 1
        elif rank == 'J':
            self.rank = 11
        elif rank == 'Q':
            self.rank = 12
        elif rank == 'K':
            self.rank = 13
        else:
            self.rank = rank

    def rank(self):
        return self.rank

    def print(self):
        print(self.rank())
