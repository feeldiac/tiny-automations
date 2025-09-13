import datetime
from src.discord_greetings_01.constants.data import dicc

def get_message():
    weekday = datetime.datetime.today().weekday()
    today = dicc[weekday]["spanishName"].lower()

    return f"Buenos días, feliz {today}."