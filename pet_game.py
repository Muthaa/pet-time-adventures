import time
import json
import os
import platform
from pet import Pet

SAVE_FILE = "pet_save.json"

def clear_screen():
    # Clears the terminal screen
    os.system("cls" if platform.system() == "Windows" else "clear")

def show_banner():
    banner = r"""
   ____      _   _   _                        _                 
  |  _ \ ___| |_| |_(_)_ __   __ _   _ __ ___| |_   _ _ __ ___  
  | |_) / _ \ __| __| | '_ \ / _` | | '__/ _ \ | | | | '_ ` _ \ 
  |  __/  __/ |_| |_| | | | | (_| |_| | |  __/ | |_| | | | | | |
  |_|   \___|\__|\__|_|_| |_|\__, (_)_|  \___|_|\__,_|_| |_| |_|
                             |___/                              

                 🐶🐱 Welcome to PetTime Adventures! 🐰🦊
    Adopt a pet, take care of it, teach it tricks, and go on adventures!
    """
    print(banner)
    print_pet_ascii()

def print_pet_ascii():
    pet_art = r"""
           /^-----^\
          V  o o  V
              Y   
           \  v  /
           / -.- \
                     ~ I'm ready to be your best buddy!
    """
    print(pet_art)

def show_menu():
    print("""
What would you like to do?
1. Feed your pet
2. Let your pet sleep
3. Play with your pet
4. Train a trick
5. Show learned tricks
6. View pet status
7. Random Event
8. Quit
""")

def choose_food(pet):
    print("Available food:")
    for food, qty in pet.inventory.items():
        print(f"- {food}: {qty}")
    choice = input("Enter food name to feed: ").strip().lower()
    pet.eat(choice)

def save_pet(pet):
    with open(SAVE_FILE, "w") as f:
        json.dump(pet.to_dict(), f)
    print("💾 Progress saved!")

def load_pet():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        return Pet.from_dict(data)
    return None

def main():
    clear_screen()
    show_banner()
    time.sleep(1.5)

    choice = input("\nDo you want to load your saved pet (L) or adopt a new one (A)? ").strip().lower()

    if choice == "l":
        pet = load_pet()
        if pet:
            print(f"\n🐾 Welcome back! {pet.name} missed you!")
        else:
            print("\n⚠️ No saved pet found. Let's adopt a new one!")
            name = input("🐾 Name your new pet: ").strip().capitalize()
            pet = Pet(name)
            print(f"\n🎉 Congratulations! You adopted {name}!")
    elif choice == "a":
        name = input("🐾 Name your new pet: ").strip().capitalize()
        pet = Pet(name)
        print(f"\n🎉 Congratulations! You adopted {name}!")
    else:
        print("\n❌ Invalid choice. Starting a new pet adoption.")
        name = input("🐾 Name your new pet: ").strip().capitalize()
        pet = Pet(name)
        print(f"\n🎉 Congratulations! You adopted {name}!")

    time.sleep(1.5)

    while True:
        clear_screen()
        print(f"🐾 Pet: {pet.name} | ❤️ Health: {pet.health} | 😋 Hunger: {pet.hunger} | ⚡ Energy: {pet.energy} | 😀 Happiness: {pet.happiness}")
        print("-" * 60)

        time.sleep(1.2)
        pet.decay()

        if pet.is_game_over():
            print(f"\n💔 Oh no! {pet.name} is gone. Take better care next time!")
            break

        show_menu()
        choice = input(">> ").strip()

        if choice == "1":
            choose_food(pet)
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            pet.train()
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            pet.random_event()
        elif choice == "8":
            save_pet(pet)
            print(f"\n🐾👋 Goodbye! {pet.name} will miss you!")
            break
        else:
            print("❌ Invalid choice. Try again.")

        time.sleep(2)

if __name__ == "__main__":
    main()
