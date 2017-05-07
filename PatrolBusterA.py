# Remember that enemies may not yet exist.
def attackNearest():
    if enemy:
        # If there is an enemy, attack it!
        hero.attack(enemy)
        pass
    
while True:
    enemy = hero.findNearestEnemy()
    attackNearest(enemy)
    
