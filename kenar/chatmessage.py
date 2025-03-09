from enum import Enum
from pydantic import BaseModel
from typing import Optional


class BotButton(BaseModel):
    class Action(Enum):
        LINK = "LINK"
        DIRECT_LINK = "DIRECT_LINK"

    class ButtonData(BaseModel):
        icon_name: str
        extra_data: dict = {}
        caption: str
        direct_link: str

    data: ButtonData
    action: Action


class SendMessageV2Request(BaseModel):
    user_id: str
    peer_id: str
    post_token: str
    type: str = "TEXT"
    message: str
    sender_btn: Optional[BotButton]
    receiver_btn: Optional[BotButton]


class SendMessageV2Response(BaseModel):
    status: int
    message: str


class PostConversationsNotificationRegisterPayload(BaseModel):
    post_token: str
    phone: str = None
    endpoint: str


class PostConversationsNotificationPayload(BaseModel):
    registration_payload: PostConversationsNotificationRegisterPayload
    identification_key: str


class ChatBotSendMessageRequest(BaseModel):
    conversation_id: Optional[str]
    user_id: Optional[str]
    text_message: str
    media_token: Optional[str]
    buttons: Optional[BotButton]


class ChatBotSendMessageResponse(BaseModel):
    pass
