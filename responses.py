from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'bye' in lowered:
        return 'Good bye, see ya later!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice([
            "I'm not sure I caught all of that.",
            "I might have missed something there.",
            "That didn't quite land with me.",
            "I think I'm a bit lost here.",
            "I'm having trouble following along.",
            "That part didn't completely register with me.",
            "I'm not entirely sure I got that.",
            "I didn't quite follow that.",
            "That didn't come through clearly for me.",
            "I feel like I'm missing something important here.",
            "I'm not sure we're on the same page.",
            "That seems a bit unclear to me.",
            "I think I missed the point there.",
            "Something about that didn't quite click for me.",
            "I'm not sure that made sense to me.",
            "That flew over my head a little."
        ])