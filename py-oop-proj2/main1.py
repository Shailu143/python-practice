# Class inheritance example. Inheritance usefullness
# Link to video https://youtu.be/Ej_02ICOIgs?si=t3S2BfeTjSP4-0sW
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, amount):
        self.health -= amount

class Warrier(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.toughness_modifier = 0.90
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)

warrier = Warrier(100,50,10)
print(f'Initial Health: {warrier.health}')
warrier.take_damage(40)
print(f'Health after damage: {warrier.health}')
