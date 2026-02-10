from pydantic import BaseModel

class Character(BaseModel):
    name: str
    level: int
    health: int

    def display_info(self):
        '''
        Returns:
        str: A formatted string with the character's name, level, and health.
        '''
        return f"{self.name} (Level: {self.level}) - {self.health} HP"