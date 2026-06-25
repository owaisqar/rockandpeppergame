import random


def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie"
        elif (
            (p1_play == "R" and p2_play == "S") or
            (p1_play == "P" and p2_play == "R") or
            (p1_play == "S" and p2_play == "P")
        ):
            results["p1"] += 1
            winner = "Player 1"
        else:
            results["p2"] += 1
            winner = "Player 2"

        if verbose:
            print(f"Player 1: {p1_play} | Player 2: {p2_play} | Winner: {winner}")

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    win_rate = results["p1"] / num_games * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate:.2f}%")

    return win_rate


def quincy(prev_play, counter=[0]):
    choices = ["R", "R", "P", "P", "S"]
    play = choices[counter[0] % len(choices)]
    counter[0] += 1
    return play


def kris(prev_play):
    if prev_play == "":
        return "R"
    ideal_response = {"R": "P", "P": "S", "S": "R"}
    return ideal_response[prev_play]


def abbey(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return "R"

    last_two = "".join(opponent_history[-2:])
    play_order = {
        "RR": "P",
        "RP": "S",
        "RS": "R",
        "PR": "P",
        "PP": "S",
        "PS": "R",
        "SR": "P",
        "SP": "S",
        "SS": "R",
    }

    return play_order[last_two]


def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 10:
        return "S"

    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    ideal_response = {"R": "P", "P": "S", "S": "R"}
    return ideal_response[most_frequent]