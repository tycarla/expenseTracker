"""
Expense Entry Form: Date, Categoy, Amount, Description

Functionality:
[INPUT]
--User can add entry forms

[PROCESS]
--User interaction
--Expense calculation
--Error handling
--Data handling (csv or sql)

[OUTPUT]
--Can view the expense by category, date, amount
--Can view summary report (e.g total monthly spending)

"""
#League Champions
# health, attack points and method to "Flight"
# defending and attacking sided
# monsters with abilities

class Monster:
    
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def fight(self, target):
        target.hp -= self.attack
        print(f"{self.name} attacked {target.name} for {self.attack} damage!")
        print(f"{target.name} has {target.hp} HP left")
        
    

Morgana = Monster("Morgana", 100, 25)
Lux = Monster("Lux", 50, 35)
Morgana.fight(Lux)
Lux.fight(Morgana)