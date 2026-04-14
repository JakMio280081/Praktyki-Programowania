class TennisGame1:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self._is_draw():
            return self._draw_score()

        if self._is_endgame():
            return self._advantage_or_win()

        return self._normal_score()

    def _is_draw(self):
        return self.p1points == self.p2points

    def _draw_score(self):
        if self.p1points < 3:
            return f"{self.SCORE_NAMES[self.p1points]}-All"
        return "Deuce"

    def _is_endgame(self):
        return self.p1points >= 4 or self.p2points >= 4

    def _advantage_or_win(self):
        diff = self.p1points - self.p2points

        if diff == 1:
            return f"Advantage {self.player1_name}"
        if diff == -1:
            return f"Advantage {self.player2_name}"
        if diff >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _normal_score(self):
        return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"
