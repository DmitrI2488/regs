

from telethon.sync import TelegramClient
from telethon import functions, types
# with TelegramClient(name, api_id, api_hash) as client:
#     result = client(functions.account.ResetAuthorizationRequest(hash=-12398745604826))
# print(result)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest

client = TelegramClient("data/79062945669", api_id=21724, api_hash="3e0cb5efcd52300aec5994fdfc5bdc16")
client.connect()
client(get_entity('https://t.me/+VQ11Kv5glfplMjU6'))
print(client.is_user_authorized())