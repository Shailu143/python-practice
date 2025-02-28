# Class inheritance example. Plain inheritance
# Link to video https://youtu.be/Ej_02ICOIgs?si=t3S2BfeTjSP4-0sW
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, amount):
        self.health -= amount

class Warrier(Character):
    pass

warrier = Warrier(100,50,10)
print(f'Initial Health: {warrier.health}')
warrier.take_damage(40)
print(f'Health after damage: {warrier.health}')
