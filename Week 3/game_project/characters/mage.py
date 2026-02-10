from .character import Character

class Mage(Character):
    def __init__(self, name, level, health, mana):
        super().__init__(name, level, health)
        # Initialize the mage's specific attribute: mana
        self.mana = mana

    # Right cast_spell method that uses mana_cost and updates self.mana
    def cast_spell(self, mana_cost):
        '''
        Simulates the mage casting a spell.
        
        Returns:
            str: A message indicating the spellcasting action.
            mana: Update the self.mana according to the mana_cost spent.
        '''

        # Could include if/else to avoid negative mana (but not enough time to do that)
        self.mana -= mana_cost
        return f"{self.name} casts spell using {mana_cost} mana! They now have {self.mana} mana."
        