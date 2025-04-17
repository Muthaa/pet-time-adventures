import random
import time
import json

class Pet:
    ascii_art = {
        "😊 Happy": r"""
 /\_/\ 
( ^.^ )  ~ I'm feeling great!
 > ^ <""",
        "😴 Tired": r"""
|\_/|                   
( -.- ) zzz            
(")_(")                
""",
        "😫 Hungry": r"""
(◕︵◕)  *grumble* I'm starving...
""",
        "😢 Sad": r"""
(；⌣̀_⌣́) I feel neglected...
""",
        "😐 Okay": r"""
(¬‿¬) Just chillin'
"""
    }

    preset_tricks = ["Sit", "Roll over", "Fetch", "High Five", "Dance", "Spin"]

    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.health = 10
        self.tricks = []
        self.unattended_cycles = 0
        self.personality = random.choice(["playful", "lazy", "curious", "hungry"])
        self.favorite_trick = None
        self.xp = 0
        self.level = 1
        self.inventory = {"kibble": 3, "treat": 2, "fish": 1}

    def to_dict(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness,
            "health": self.health,
            "tricks": self.tricks,
            "unattended_cycles": self.unattended_cycles,
            "personality": self.personality,
            "favorite_trick": self.favorite_trick,
            "xp": self.xp,
            "level": self.level,
            "inventory": self.inventory,
        }

    @classmethod
    def from_dict(cls, data):
        pet = cls(data["name"])
        pet.hunger = data["hunger"]
        pet.energy = data["energy"]
        pet.happiness = data["happiness"]
        pet.health = data["health"]
        pet.tricks = data["tricks"]
        pet.unattended_cycles = data["unattended_cycles"]
        pet.personality = data["personality"]
        pet.favorite_trick = data["favorite_trick"]
        pet.xp = data["xp"]
        pet.level = data["level"]
        pet.inventory = data["inventory"]
        return pet

    def eat(self, food="kibble"):
        if food not in self.inventory or self.inventory[food] <= 0:
            print(f"No {food} left in inventory!")
            return

        self.inventory[food] -= 1
        if food == "kibble":
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
        elif food == "treat":
            self.hunger = max(0, self.hunger - 2)
            self.happiness = min(10, self.happiness + 2)
        elif food == "fish":
            self.hunger = max(0, self.hunger - 5)
            self.health = min(10, self.health + 2)

        self.gain_xp(3)
        print(f"{self.name} enjoyed the {food}!")

    def sleep(self):
        print(f"{self.name} is sleeping... 😴")
        time.sleep(1)
        self.energy = min(10, self.energy + 5)
        self.happiness = min(10, self.happiness + 1)
        self.health = min(10, self.health + 1)
        self.gain_xp(3)

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
        else:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            self.gain_xp(4)
            print(f"{self.name} had fun playing!")

    def train(self):
        available = [t for t in self.preset_tricks if t not in self.tricks]
        if not available:
            print(f"{self.name} has learned all the tricks!")
            return
        trick = random.choice(available)
        self.tricks.append(trick)
        self.favorite_trick = trick if not self.favorite_trick else self.favorite_trick
        self.happiness = min(10, self.happiness + 2)
        self.gain_xp(5)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        mood = self.get_mood()
        print(f"\n🐾 {self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10 | Energy: {self.energy}/10 | Happiness: {self.happiness}/10 | Health: {self.health}/10")
        print(f"XP: {self.xp} | Level: {self.level} | Mood: {mood} | Personality: {self.personality}")
        if self.favorite_trick:
            print(f"Favorite Trick: {self.favorite_trick}")
        print("🎒 Inventory:", self.inventory)
        print(self.ascii_art[mood])
        print("-" * 40)

    def get_mood(self):
        if self.happiness > 7:
            return "😊 Happy"
        elif self.energy < 3:
            return "😴 Tired"
        elif self.hunger > 7:
            return "😫 Hungry"
        elif self.happiness < 3:
            return "😢 Sad"
        return "😐 Okay"

    def talk(self):
        if self.hunger > 7:
            print(f"{self.name} says: I'm starving! 🥺")
        elif self.happiness < 4:
            print(f"{self.name} says: I’m feeling kinda down... 💧")
        else:
            print(f"{self.name} says: You're the best! 🐾")

    def decay(self):
        self.hunger = min(10, self.hunger + 1)
        self.energy = max(0, self.energy - 1)
        self.happiness = max(0, self.happiness - 1)

        if self.energy <= 2:
            print(f"{self.name} is exhausted and needs sleep.")
            self.sleep()

        if self.hunger >= 9 or self.happiness <= 2:
            self.unattended_cycles += 1
        else:
            self.unattended_cycles = 0

        self.random_event()
        self.level_up()

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        print(f"\n🎉 LEVEL UP! {self.name} is now level {self.level}! 🎉")
        print("✨ Your pet feels stronger and more confident! ✨")
        print("-" * 40)        

    def random_event(self):
        events = [
            lambda: print(f"🌧️ It rained today. {self.name} played in the puddles!"),
            lambda: print(f"🎁 You found a gift for {self.name}! Happiness +2") or self.modify_happiness(2),
            lambda: print(f"🤒 {self.name} is feeling a bit sick. Health -2") or self.modify_health(-2),
            lambda: print(f"🐦 {self.name} made a new bird friend at the park."),
            lambda: print(f"    {self.name} found a toy.") or self.modify_happiness(+2),
        ]
        random.choice(events)()

    def modify_happiness(self, amount):
        self.happiness = max(0, min(10, self.happiness + amount))

    def modify_health(self, amount):
        self.health = max(0, min(10, self.health + amount))

    def is_game_over(self):
        if self.unattended_cycles >= 5:
            print(f"\n💔 {self.name} ran away due to neglect...")
            return True
        return False

    # Save the pet's state to a JSON file
    def save_to_json(self, filename):
        pet_data = {
            'name': self.name,
            'hunger': self.hunger,
            'energy': self.energy,
            'happiness': self.happiness,
            'health': self.health,
            'tricks': self.tricks,
            'unattended_cycles': self.unattended_cycles,
            'personality': self.personality,
            'favorite_trick': self.favorite_trick,
            'xp': self.xp,
            'level': self.level,
            'inventory': self.inventory
        }
        with open(filename, 'w') as f:
            json.dump(pet_data, f, indent=4)
        print(f"{self.name}'s state has been saved to {filename}.")

    # Load the pet's state from a JSON file
    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r') as f:
            pet_data = json.load(f)
        
        pet = cls(pet_data['name'])
        pet.hunger = pet_data['hunger']
        pet.energy = pet_data['energy']
        pet.happiness = pet_data['happiness']
        pet.health = pet_data['health']
        pet.tricks = pet_data['tricks']
        pet.unattended_cycles = pet_data['unattended_cycles']
        pet.personality = pet_data['personality']
        pet.favorite_trick = pet_data['favorite_trick']
        pet.xp = pet_data['xp']
        pet.level = pet_data['level']
        pet.inventory = pet_data['inventory']
        
        print(f"{pet.name}'s state has been loaded from {filename}.")
        return pet
