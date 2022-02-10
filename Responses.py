from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hallo", "hey", "sup", "hi",):
        return "hello you, how are you doing!"

    if user_message in ("how are you","how are you?", "how are u?", "how are u",):
        return "i am doing well as a bot, ty"

    if user_message in ("time","time?", "what is the time now", "what time is it"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    return "I do not understand ew?"
    
