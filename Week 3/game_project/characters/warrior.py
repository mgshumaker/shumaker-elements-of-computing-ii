from .character import Character

# Subclass Example: Warrior
class Warrior(Character):

    #default template
    def __init__(self, name, level, health, strength):
        #super() calls the init attributes from Character
        super().__init__(name, level, health)
        self.strength = strength