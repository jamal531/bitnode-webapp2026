import random

def get_prediction():
    choices = ['UP', 'DOWN']
    return {
        'pair': 'EUR/USD OTC',
        'timeframe': '1M',
        'next_2_candles': [random.choice(choices), random.choice(choices)],
        'confidence': f"{random.randint(85, 99)}%"
    }
