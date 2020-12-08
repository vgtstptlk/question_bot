import vk_api
from secret import secret
from QuestionParse import QuestionParse
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

def send_user_message(usr_id, msg):
    vk.messages.send(
        user_id=usr_id,
        message=msg,
        random_id=random.randint(1, 2147123123))


def send_group_message(cht_id, msg):
    vk.messages.send(
        key=secret.key,
        server=secret.server,
        ts="1",
        chat_id=cht_id,
        message=msg,
        random_id=get_random_id())


vk_session = vk_api.VkApi(token=secret.vk_token2)
longpoll = VkBotLongPoll(vk_session, 200879438)
vk = vk_session.get_api()

parse = QuestionParse()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.message['text'] == '/new' or event.message['text'] == '/новые':

            if event.from_chat:
                print(event.chat_id)
                send_group_message(event.chat_id, parse.get_new_messages())

        if event.message['text'] == '/all':
            if event.from_chat:
                send_group_message(event.chat_id, parse.get_all_messages())
