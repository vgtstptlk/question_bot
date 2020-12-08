from QuestionParse import QuestionParse
from api_vk import Vk


parse = QuestionParse()
vk = Vk()
vk.send_group_message(1, "АВТОМАТИЧЕСКАЯ РАССЫЛКА (@all) \n"+parse.get_new_messages())

