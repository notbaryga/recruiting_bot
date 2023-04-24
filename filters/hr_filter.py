from aiogram.filters import BaseFilter
from aiogram.types import Message

from models.base import base1

class IsHR(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if base1.get_user(message.from_user.id) is not None:
            return base1.get_role(message.from_user.id)[0] == 'employer'
        else:
            return False
