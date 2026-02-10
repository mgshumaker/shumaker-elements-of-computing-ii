from .warrior import Warrior

# Coding Challenge: Add Your Own Class
class Rogue(Warrior):
    # Initialize warrior attributes
    def __init__(self, name, level, health, strength, stealth):
        # Inherit attributes
        super().__init__(name, level, health, strength)
        # Initialize the Rogue's specific attribute: stealth
        self.stealth = stealth
    # Create sneak attack that targets and reduces health of another player
    def sneak_attack(self, target):
        '''
        Sneak attacks the target character!

        Args:
            self (Rogue): Use the strength//stealth attr as attack level.
            target (Character): Character to attack.

        Returns:
            str: A message indicating attack action
        '''
        # Reduce the target's health by a factor of stealth
        target.health -= (self.strength//self.stealth)
        # Return a message describing the sneak attack action
        return f"{self.name} sneakily strikes {target.name} for {self.strength//self.stealth} hp! {target.name} now has {target.health} health."