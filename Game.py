#! /usr/bin/python3

class Player:
	def __init__(self, name, race):
		self.name = name
		self.race = race
		self.Level = 1
		self.Health = 400
		self.Mana = 150
		self.Damage = 35
		self.Armor = 1
		self.Strength = 15
		self.Agility = 14
		self.Intelligence = 13

	def __str__(self):
		return("{} is a {}".format(self.name, self.race))

	def Levelup(self):
		self.Level += 1
		self.Health += 38
		self.Mana += 26
		self.Damage += 2
		self.Armor += 0.3
		self.Strength += 2
		self.Agility += 2
		self.Intelligence += 2

class Assasins(Player):

	def __init__(self, name, race):
		Player.__init__(self, name, race)
		self.Health = 530
		self.Mana = 182
		self.Damage = 54
		self.Armor = 4
		self.Strength = 20
		self.Agility = 26
		self.Intelligence = 14

	def __str__(self):
		return("{} is an {}".format(self.name, self.race))

class Fighter(Player):

	def __init__(self, name, race):
		Player.__init__(self, name, race)
		self.Health = 530
		self.Mana = 221
		self.Damage = 61
		self.Armor = 5
		self.Strength = 20
		self.Agility = 15
		self.Intelligence = 17

class Giant(Player):

	def __init__(self, name, race):
		Player.__init__(self, name, race)
		self.Health = 587
		self.Mana = 221
		self.Damage = 64
		self.Armor = 7
		self.Strength = 23
		self.Agility = 14
		self.Intelligence = 17

class Mage(Player):

	def __init__(self, name, race):
		Player.__init__(self, name, race)
		self.Health = 454
		self.Mana = 208
		self.Damage = 41
		self.Armor = 1
		self.Strength = 16
		self.Agility = 16
		self.Intelligence = 16

class Sniper(Player):
	
	def __init__(self, name, race):
		Player.__init__(self, name, race)
		self.Health = 473
		self.Mana = 195
		self.Damage = 55
		self.Armor = 1
		self.Strength = 17
		self.Agility = 26
		self.Intelligence = 15

class Unknown(Player):

	def __str__(self):
		return("{} is an {} player".format(self.name, self.race))

Mahdi = Assasins("Mahdi", "Assasins")
print(Mahdi)

print("")

print("Level:", Mahdi.Level)
print("Health:", Mahdi.Health)
print("Mana:", Mahdi.Mana)
print("Damage:", Mahdi.Damage)
print("Armor:", Mahdi.Armor)
print("Strength:", Mahdi.Strength)
print("Agility:", Mahdi.Agility)
print("Intelligence:", Mahdi.Intelligence)
print("First power: Blade Fury")

print("")
print("Level up")
print("")

Mahdi.Levelup()
print("Level:", Mahdi.Level)
print("Health:", Mahdi.Health)
print("Mana:", Mahdi.Mana)
print("Damage:", Mahdi.Damage)
print("Armor:", Mahdi.Armor)
print("Strength:", Mahdi.Strength)
print("Agility:", Mahdi.Agility)
print("Intelligence:", Mahdi.Intelligence)
print("First power: Blade Fury")
print("Second power: Healing Ward")

print("")
print("Level up")
print("")

Mahdi.Levelup()
print("Level:", Mahdi.Level)
print("Health:", Mahdi.Health)
print("Mana:", Mahdi.Mana)
print("Damage:", Mahdi.Damage)
print("Armor:", Mahdi.Armor)
print("Strength:", Mahdi.Strength)
print("Agility:", Mahdi.Agility)
print("Intelligence:", Mahdi.Intelligence)
print("First power: Blade Fury")
print("Second power: Healing Ward")
print("Third power: Blade Dance")

print("")
print("Level up")
print("")

Mahdi.Levelup()
print("Level:", Mahdi.Level)
print("Health:", Mahdi.Health)
print("Mana:", Mahdi.Mana)
print("Damage:", Mahdi.Damage)
print("Armor:", Mahdi.Armor)
print("Strength:", Mahdi.Strength)
print("Agility:", Mahdi.Agility)
print("Intelligence:", Mahdi.Intelligence)
print("First power: Blade Fury")
print("Second power: Healing Ward")
print("Third power: Blade Dance")
print("Fourth power: Omnislash")

print("")

Mobin = Fighter("Mobin", "Fighter")
print(Mobin)

print("")

print("Level:", Mobin.Level)
print("Health:", Mobin.Health)
print("Mana:", Mobin.Mana)
print("Damage:", Mobin.Damage)
print("Armor:", Mobin.Armor)
print("Strength:", Mobin.Strength)
print("Agility:", Mobin.Agility)
print("Intelligence:", Mobin.Intelligence)
print("First power: Purification")

print("")
print("Level up")
print("")

Mobin.Levelup()
print("Level:", Mobin.Level)
print("Health:", Mobin.Health)
print("Mana:", Mobin.Mana)
print("Damage:", Mobin.Damage)
print("Armor:", Mobin.Armor)
print("Strength:", Mobin.Strength)
print("Agility:", Mobin.Agility)
print("Intelligence:", Mobin.Intelligence)
print("First power: Purification")
print("Second power: Repel")

print("")
print("Level up")
print("")

Mobin.Levelup()
print("Level:", Mobin.Level)
print("Health:", Mobin.Health)
print("Mana:", Mobin.Mana)
print("Damage:", Mobin.Damage)
print("Armor:", Mobin.Armor)
print("Strength:", Mobin.Strength)
print("Agility:", Mobin.Agility)
print("Intelligence:", Mobin.Intelligence)
print("First power: Purification")
print("Second power: Repel")
print("Third power: Degen Aura")

print("")
print("Level up")
print("")

Mobin.Levelup()
print("Level:", Mobin.Level)
print("Health:", Mobin.Health)
print("Mana:", Mobin.Mana)
print("Damage:", Mobin.Damage)
print("Armor:", Mobin.Armor)
print("Strength:", Mobin.Strength)
print("Agility:", Mobin.Agility)
print("Intelligence:", Mobin.Intelligence)
print("First power: Purification")
print("Second power: Repel")
print("Third power: Degen Aura")
print("Fourth power: Guardian Angel")

print("")

Ali = Giant("Ali", "Giant")
print(Ali)

print("")

print("Level:", Ali.Level)
print("Health:", Ali.Health)
print("Mana:", Ali.Mana)
print("Damage:", Ali.Damage)
print("Armor:", Ali.Armor)
print("Strength:", Ali.Strength)
print("Agility:", Ali.Agility)
print("Intelligence:", Ali.Intelligence)
print("First power: Fireblast")

print("")
print("Level up")
print("")

Ali.Levelup()
print("Level:", Ali.Level)
print("Health:", Ali.Health)
print("Mana:", Ali.Mana)
print("Damage:", Ali.Damage)
print("Armor:", Ali.Armor)
print("Strength:", Ali.Strength)
print("Agility:", Ali.Agility)
print("Intelligence:", Ali.Intelligence)
print("First power: Fireblast")
print("Second power: Ignite")

print("")
print("Level up")
print("")

Ali.Levelup()
print("Level:", Ali.Level)
print("Health:", Ali.Health)
print("Mana:", Ali.Mana)
print("Damage:", Ali.Damage)
print("Armor:", Ali.Armor)
print("Strength:", Ali.Strength)
print("Agility:", Ali.Agility)
print("Intelligence:", Ali.Intelligence)
print("First power: Fireblast")
print("Second power: Ignite")
print("Third power: Bloodlust")

print("")
print("Level up")
print("")

Ali.Levelup()
print("Level:", Ali.Level)
print("Health:", Ali.Health)
print("Mana:", Ali.Mana)
print("Damage:", Ali.Damage)
print("Armor:", Ali.Armor)
print("Strength:", Ali.Strength)
print("Agility:", Ali.Agility)
print("Intelligence:", Ali.Intelligence)
print("First power: Fireblast")
print("Second power: Ignite")
print("Third power: Bloodlust")
print("Fourth power: Multi Cast")

print("")

Mahsa = Mage("Mahsa", "Mage")
print(Mahsa)

print("")

print("Level:", Mahsa.Level)
print("Health:", Mahsa.Health)
print("Mana:", Mahsa.Mana)
print("Damage:", Mahsa.Damage)
print("Armor:", Mahsa.Armor)
print("Strength:", Mahsa.Strength)
print("Agility:", Mahsa.Agility)
print("Intelligence:", Mahsa.Intelligence)
print("First power: Crystal Nova")

print("")
print("Level up")
print("")

Mahsa.Levelup()
print("Level:", Mahsa.Level)
print("Health:", Mahsa.Health)
print("Mana:", Mahsa.Mana)
print("Damage:", Mahsa.Damage)
print("Armor:", Mahsa.Armor)
print("Strength:", Mahsa.Strength)
print("Agility:", Mahsa.Agility)
print("Intelligence:", Mahsa.Intelligence)
print("First power: Crystal Nova")
print("Second power: Frostbite")

print("")
print("Level up")
print("")

Mahsa.Levelup()
print("Level:", Mahsa.Level)
print("Health:", Mahsa.Health)
print("Mana:", Mahsa.Mana)
print("Damage:", Mahsa.Damage)
print("Armor:", Mahsa.Armor)
print("Strength:", Mahsa.Strength)
print("Agility:", Mahsa.Agility)
print("Intelligence:", Mahsa.Intelligence)
print("First power: Crystal Nova")
print("Second power: Frostbite")
print("Third power: Brilliance Aura")

print("")
print("Level up")
print("")

Mahsa.Levelup()
print("Level:", Mahsa.Level)
print("Health:", Mahsa.Health)
print("Mana:", Mahsa.Mana)
print("Damage:", Mahsa.Damage)
print("Armor:", Mahsa.Armor)
print("Strength:", Mahsa.Strength)
print("Agility:", Mahsa.Agility)
print("Intelligence:", Mahsa.Intelligence)
print("First power: Crystal Nova")
print("Second power: Frostbite")
print("Third power: Brilliance Aura")
print("Fourth power: Freezing Field")

print("")

Zahra = Sniper("Zahra", "Sniper")
print(Zahra)

print("")

print("Level:", Zahra.Level)
print("Health:", Zahra.Health)
print("Mana:", Zahra.Mana)
print("Damage:", Zahra.Damage)
print("Armor:", Zahra.Armor)
print("Strength:", Zahra.Strength)
print("Agility:", Zahra.Agility)
print("Intelligence:", Zahra.Intelligence)
print("First power: Frost Arrows")

print("")
print("Level up")
print("")

Zahra.Levelup()
print("Level:", Zahra.Level)
print("Health:", Zahra.Health)
print("Mana:", Zahra.Mana)
print("Damage:", Zahra.Damage)
print("Armor:", Zahra.Armor)
print("Strength:", Zahra.Strength)
print("Agility:", Zahra.Agility)
print("Intelligence:", Zahra.Intelligence)
print("First power: Frost Arrows")
print("Second power: Gust")

print("")
print("Level up")
print("")

Zahra.Levelup()
print("Level:", Zahra.Level)
print("Health:", Zahra.Health)
print("Mana:", Zahra.Mana)
print("Damage:", Zahra.Damage)
print("Armor:", Zahra.Armor)
print("Strength:", Zahra.Strength)
print("Agility:", Zahra.Agility)
print("Intelligence:", Zahra.Intelligence)
print("First power: Frost Arrows")
print("Second power: Gust")
print("Third power: Trueshot Aura")

print("")
print("Level up")
print("")

Zahra.Levelup()
print("Level:", Zahra.Level)
print("Health:", Zahra.Health)
print("Mana:", Zahra.Mana)
print("Damage:", Zahra.Damage)
print("Armor:", Zahra.Armor)
print("Strength:", Zahra.Strength)
print("Agility:", Zahra.Agility)
print("Intelligence:", Zahra.Intelligence)
print("First power: Frost Arrows")
print("Second power: Gust")
print("Third power: Trueshot Aura")
print("Fourth power: Marksmanship")

print("")

Samane = Unknown("Samane", "Unknown")
print(Samane)

print("")

print("Level:", Samane.Level)
print("Health:", Samane.Health)
print("Mana:", Samane.Mana)
print("Damage:", Samane.Damage)
print("Armor:", Samane.Armor)
print("Strength:", Samane.Strength)
print("Agility:", Samane.Agility)
print("Intelligence:", Samane.Intelligence)
print("First Skill : ????")

print("")
print("Next Level")
print("")

Samane.Levelup()
print("Level:", Samane.Level)
print("Health:", Samane.Health)
print("Mana:", Samane.Mana)
print("Damage:", Samane.Damage)
print("Armor:", Samane.Armor)
print("Strength:", Samane.Strength)
print("Agility:", Samane.Agility)
print("Intelligence:", Samane.Intelligence)
print("First Skill : ????")
print("Second Skill : ????")

print("")
print("Next Level")
print("")

Samane.Levelup()
print("Level:", Samane.Level)
print("Health:", Samane.Health)
print("Mana:", Samane.Mana)
print("Damage:", Samane.Damage)
print("Armor:", Samane.Armor)
print("Strength:", Samane.Strength)
print("Agility:", Samane.Agility)
print("Intelligence:", Samane.Intelligence)
print("First Skill : ????")
print("Second Skill : ????")
print("Third Skill : ????")

print("")
print("Next Level")
print("")

Samane.Levelup()
print("Level:", Samane.Level)
print("Health:", Samane.Health)
print("Mana:", Samane.Mana)
print("Damage:", Samane.Damage)
print("Armor:", Samane.Armor)
print("Strength:", Samane.Strength)
print("Agility:", Samane.Agility)
print("Intelligence:", Samane.Intelligence)
print("First Skill : ????")
print("Second Skill : ????")
print("Third Skill : ????")
print("fourth Skill : ????")


