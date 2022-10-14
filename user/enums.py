from enum import Enum


class Role(Enum):
    SUPER_MANAGER = 20
    MANAGER = 10
    ADMIN = 5
    EXECUTIVE = 1


roles = [*Role.__members__.keys()]
