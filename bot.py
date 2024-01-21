import requests
from settings import URL,car
from time import sleep
from bored.main import Bored


welcome_msg = '''
<b>Hello there!</b>

🌟 Welcome to the Random Advice Bot! 🌟

Get ready to receive a dose of wisdom and guidance tailored just for you. Here's a quick guide on how to make the most out of this bot:

1. <b>/start:</b> Use this command to receive a warm welcome message and get instructions on how to interact with the bot.

2. /random: Feeling spontaneous? Use this command for a random piece of advice that might just be what you need at the moment.

3. /sport: Need advice related to sports? Type this command, and let the bot serve you some sports-related wisdom.

4. /education: If you're seeking guidance on matters of education, use this command to receive valuable advice.

5. /recreational: For advice on leisure and recreational activities, simply type this command and enjoy some thoughtful suggestions.

6. /social: Looking for tips on social interactions? Use this command to receive advice that could enhance your social experiences.

7. /diy: Planning a DIY project? Type this command to get some helpful advice for your do-it-yourself endeavors.

8. /cooking: Ready to whip up a delicious meal? Use this command for cooking advice that might just make your culinary experience even better.

9. /relaxation: Feeling stressed? Type this command for advice on relaxation techniques that could help you unwind.

10. /busywork: Need something to keep yourself occupied? Use this command for advice on productive and engaging tasks.

Remember, if you enter any other text, the bot will provide an error message to guide you back to the available commands.
'''


def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url =URL+endpoint
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']

        if len(result) != 0:
            return result[-1]
        else:
            return 404
    return response.status_code

def send_message(url: str, chat_id: int, text: str):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.get(url, params=payload)


def main(url: str):
    bored = Bored()
    last_update_id = -1
    while True:
        curr_update = get_last_update(url)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')

            if text is None:
                send_message(url, user['id'], 'Send text message')

            elif text == '/start':
                send_message(url, user['id'], welcome_msg)

            elif text == '/random':
                advice = bored.get_activity()['activity']
                send_message(url, user['id'], advice)

            elif text == '/education':
                advice = bored.get_activity_by_type('education')['activity']
                send_message(url, user['id'], advice)

            elif text == '/recreational':
                advice = bored.get_activity_by_type('recreational')['activity']
                send_message(url,user['id'],advice)

            elif text =='/social':
                advice = bored.get_activity_by_type('social')['activity']
                send_message(url,user['id'],advice)

            elif text == '/diy':
                advice = bored.get_activity_by_type('diy')['activity']
                send_message(url,user['id'],advice)

            elif text == '/cooking':
                advice = bored.get_activity_by_type('cooking')['activity']
                send_message(url,user['id'],advice)

            elif text=='/relaxation':
                advice = bored.get_activity_by_type('relaxation')['activity']
                send_message(url,user['id'],advice)

            elif text == '/busywork':
                advice = bored.get_activity_by_type('busywork')['activity']
                send_message(url,user['id'],advice)
            else:
                send_message(url, user['id'], 'error message')

            last_update_id = curr_update['update_id']

        sleep(0.5)
main(URL)