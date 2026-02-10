from .warrior import Warrior

class Archer(Warrior):
    '''
    The Archer subclass of the Warrior class.
    Shoots arrows from a limited quiver of arrows.

    Attributes:
    name (str): The character's name.
    level (int): The character's level.
    health (int): The character's starting health.
    strength (int): The character's strength.
    arrows (int): The number of arrows in the Archer's quiver.
    '''
    def __init__(self, name, level, health, strength, arrows):
        super().__init__(name, level, health, strength) # Inheriting attributes from Warrior
        self.arrows = arrows                 # Initializing archer-specific arrows attribute

    def fire_arrow(self, target): # fire_arrow as in firing arrows not flaming arrows lol
        '''
        Fires an arrow from the archer's quiver.

        Args:
            self (Archer): Uses the arrows attr as ammunition and strength attr as damage dealt.
            target (Character): Character to fire arrows at.

        Returns:
            str: A message indicating combat action
        '''

        if self.arrows > 0:
            self.arrows -= 1
            target.health -= self.strength
            return f"{self.name} fired an arrow at {target.name} for {self.strength} damage!\n{self.name} has {self.arrows} arrow(s) left in their quiver."
        else:
            return f"{self.name} is out of arrows. {target.name} remains unharmed."