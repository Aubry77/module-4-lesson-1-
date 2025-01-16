import random

def mood_response(mood):
    responses = {
        "happy": ["Spread that joy! "],
        "sad": ["Awww, well there's nothing a little glitter can't fix. "],
        "excited": ["I tend to do that to people! "],
        "angry": ["Who do I need to go beat up? "],
        "tired": ["Because you've been running through my mind all day! "]
    }
    return random.choice(responses.get(mood.lower(), ["my brain ain't braining"]))

