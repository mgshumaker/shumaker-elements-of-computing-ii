from .character import Character

class Healer(Character):

    # Initialize character attributes
        # Inherit name, level, health attributes
    def __init__(self, name, level, health, healing_power):
        super().__init__(name, level, health)
        # Initialize the healer's specific attribute: healing_power
        self.healing_power = healing_power

    # Create healing method that interacts with other character
    def heal(self, target):
        '''
        Heals the target character.

        Args:
            self (Healer): Use the healing_power attr as healing points.
            target (Character): Character to heal.

        Returns:
            str: A message indicating healing action
        '''

        # Increase the target's health by the healer's healing power
        target.health += self.healing_power
        # Return a message describing the healing action
        return f"{self.name} heals {target.name} for {self.healing_power} hp. They now have {target.health} hp."