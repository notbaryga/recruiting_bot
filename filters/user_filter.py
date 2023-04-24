from aiogram.filters import BaseFilter
from aiogram.types import Message

from models.base import base


class IsUser(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return base.get_role(message.from_user.id)[0] == 'applicant'


