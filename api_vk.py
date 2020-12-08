import vk_api
from secret import secret
from vk_api.utils import get_random_id


class Vk:
    def __init__(self):
        vk_session = vk_api.VkApi(token=secret.vk_token2)
        self.vk = vk_session.get_api()

    def send_group_message(self, cht_id, msg):
        self.vk.messages.send(
            key=secret.key,
            server=secret.server,
            ts="1",
            chat_id=cht_id,
            message=msg,
            random_id=get_random_id())