def generate_scoreboard(participants):
    scoreboard = []
    for participant in participants:
        name = participant['name']
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scoreboard.append({'name': name, 'score': score})
    
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard
