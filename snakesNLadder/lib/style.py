from PyInquirer import style_from_dict, Token, prompt
style = style_from_dict({
	Token.QuestionMark: '#FFD700 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FFD700 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: ''
    })


val_dict = {
	'1. Play Game': 1,
	'2. How to Play': 2,
	'3. Show Licence': 3,
	'4. Bugs/Suggestions': 4,
	'5. Exit': 0,
	'Single Player': 1,
    'Multi Player': 2,
    'Back To Main Menu': -1,
    "Classic (Single Die)": 1,
    'Popular (Double Dice)': 2,
	}

QUESTIONS_MAIN_MENU = [
        {
        'type': 'list',
        'name': 'game_options',
        'message': 'Select An Option to Start',
        'choices': [
            '1. Play Game',
            '2. How to Play',
            '3. Show Licence',
            '4. Bugs/Suggestions',
            '5. Exit'
        ],
        'filter': lambda val: val_dict[val]
        },
        {
        'type': 'list',
        'name': 'game_mode',
        'message': 'Select Game Mode: ',
        'choices': [
            'Single Player',
            'Multi Player',
            'Back To Main Menu'],
        'when': lambda answers: answers['game_options'] == 1,
        'filter': lambda val: val_dict[val]
        },
        {
        'type': 'list',
        'name': 'dice_mode',
        'message': 'Select Game Type: ',
        'choices': [
            'Classic (Single Die)',
            'Popular (Double Dice)',
            'Back To Main Menu'],
        'when': lambda answers: 'game_mode' in answers and answers['game_mode'] != -1,
                'filter': lambda val: val_dict[val]
        },
        {
        'type': 'list',
        'name': 'no_of_players',
        'message': 'Select Number of Players: ',
        'choices': [
            '2',
            '3',
            '4'],
        'when': lambda answers: 'game_mode' in answers and answers['game_mode'] == 2,
                'filter': lambda val: int(val)
        }
        ]

EACH_MOVE_PROMPT = [

    {
        'type': 'list',
        'name': 'toBeDelivered',
        'message': "",
        'choices': ["Roll Dice For Player {player_name}"],
},]
