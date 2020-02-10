"""
lab_3.py
Author: Hamin Hong
CS344
GPS cannot solve problems where to reach a goal, the order cannot be reversed.
"""
from gps import gps

problem = {
    'initial': ['inside the helicopter', 'parachute is in the helicopter'],
    'goal': ['safely landed'],

    'actions': [
        {
            'action': 'jump',
            'preconds': [
                'inside the helicopter'
            ],
            'add': [
                'is falling'
            ],
            'delete': [
                'inside the helicopter',
            ]
        },
        {
            'action': 'grab parachute',
            'preconds': [
                'inside the helicopter',
                'parachute is in the helicopter'
            ],
            'add': [
                'has prarchut'
            ],
            'delete': [
                'has prarchut',
                'parachute is in the helicopter'
            ]            
        },
        {
            # Because GPS uses "recursion," if the order of the actions is crucial, like this case, falling and has parachute,
            # The GPS cannot solve the problem
            'action': 'open parachute',
            'preconds': [
                'is falling',
                'has prarchut'
            ],
            'add': [
                'safely landed'
            ],
            'delete': [
                'has prarchut'
            ]
            
        }
    ]
}


if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')