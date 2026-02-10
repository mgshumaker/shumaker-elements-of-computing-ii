# Defining a Base Class: Character
class Character:
    '''
    Represents a generic RPG character.

    Attributes:
    name (str): The character's name.
    level (int): The character's level.
    health (int): The character's starting health.
    '''

    # def __init(self) default template for custom classes
    def __init__(self, name: str, level: int, health: int):
        '''
        Initializes a new character object.

        Attributes:
        name (str): The character's name.
        level (int): The character's level.
        health (int): The character's current health.
        '''

        self.name = name
        self.level = level 
        self.health = health

    # Create a method that displays the character's information
    def display_info(self):
        '''
        Returns:
        str: A formatted string with the character's name, level, and health.
        '''

        return f"{self.name} (Level: {self.level}) - {self.health} HP"