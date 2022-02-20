import random

R_EATING = "I'm a robot, I don't eat anything obviously!"

def unknown():
    response=['Could you please re-phrase that?',
              "...",
              "Sounds about right...",
              "What does that mean?"][random.randrange(4)]
    return response