def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return "R"

    beats = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    # Detect Quincy pattern
    quincy_pattern = ["R", "R", "P", "P", "S"]
    if len(opponent_history) >= 5:
        last_five = opponent_history[-5:]
        if last_five == quincy_pattern:
            next_index = len(opponent_history) % 5
            return beats[quincy_pattern[next_index]]

    # Pattern prediction strategy
    n = 4
    if len(opponent_history) > n:
        pattern = "".join(opponent_history[-n:])
        possible_moves = {"R": 0, "P": 0, "S": 0}

        history_string = "".join(opponent_history)

        for i in range(len(history_string) - n):
            if history_string[i:i+n] == pattern:
                next_move = history_string[i+n]
                possible_moves[next_move] += 1

        predicted = max(possible_moves, key=possible_moves.get)

        if possible_moves[predicted] > 0:
            return beats[predicted]

    # Fallback: beat opponent's most common move
    most_common = max(set(opponent_history), key=opponent_history.count)
    return beats[most_common]