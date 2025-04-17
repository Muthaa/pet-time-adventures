**Game Name**: **PetTime Adventures**

---
# PetTime Adventures

Welcome to **PetCare Adventure**, the interactive pet care game where you can adopt, care for, and grow a lovable virtual pet. Take care of your pet's needs by feeding, playing, and training, while keeping an eye on their hunger, happiness, and health. But beware, neglecting your pet too long might lead to them running away. Will you be a good pet parent? It's all up to you!

![Windows PowerShell 17_04_2025 11_43_36](https://github.com/user-attachments/assets/dd3f1d64-895e-4b36-9e52-dcc27cef7304)


## Features

- **Adopt a Pet**: Start by adopting a new pet or continue your journey with a saved one.
- **Pet Care**: Feed, play, sleep, and train your pet to keep them happy and healthy.
- **Random Events**: Enjoy random events like finding toys, making new friends, and more to spice up the game.
- **Level Up**: As you take care of your pet, they'll gain XP and level up, unlocking new possibilities!
- **Save and Load Progress**: Save your pet’s progress and come back to continue their adventure later.

![Windows PowerShell 17_04_2025 11_44_05](https://github.com/user-attachments/assets/e6c64b3f-5fbc-4ecd-b00f-c27cfd7a2e5f)

## Gameplay

1. **Feed your pet**: Keep your pet's hunger in check by feeding them from a variety of food items in their inventory (e.g., kibble, treats, and fish).
2. **Let your pet sleep**: Recharge your pet’s energy and restore some health by letting them sleep.
3. **Play with your pet**: Keep your pet entertained and happy by playing with them. But be careful—playing too much can drain their energy.
4. **Train a trick**: Help your pet learn new tricks, and maybe even teach them their favorite trick.
5. **Show learned tricks**: Display the tricks your pet has learned along the way.
6. **View pet status**: Check on your pet’s stats, including hunger, energy, happiness, and health, to make sure they’re doing okay.
7. **Random events**: Enjoy random events that may increase happiness or cause some setbacks.
8. **Save progress**: Save your pet’s current state to continue your adventure later.

## Setup

To run **PetTime Adventures*** on your local machine:

### Requirements

- Python 3.6 or higher
- Basic knowledge of how to run Python programs

### Installation Steps

1. Clone or download the repository:

    ```bash
    git clone https://github.com/yourusername/pet-time-adventures.git
    ```

2. Navigate to the project folder:

    ```bash
    cd pet-time-adventures
    ```

3. Run the game:

    ```bash
    python pet_game.py
    ```

The game will prompt you to either adopt a new pet or load a saved one, and then you can start caring for your virtual pet!

## Game Flow

1. When you first start the game, you can choose to adopt a new pet or load a previously saved one.
2. The game will enter an interactive loop, allowing you to choose from various actions such as feeding, playing, or training.
3. Each time you take an action, the pet’s stats (like hunger, energy, happiness, and health) will be updated.
4. If you neglect your pet for too long, they might run away. Keep an eye on their status to ensure they stay happy and healthy!
5. You can save your progress at any time and load it later to continue where you left off.

## Key Concepts

- **XP & Leveling Up**: Your pet gains experience points (XP) through different actions like playing, eating, and training. Once they accumulate enough XP, they will level up, becoming stronger and more capable of handling different tasks.
- **Mood**: Your pet’s mood will change based on their needs. If they’re happy, you’ll see a "😊 Happy" face. If they’re hungry, tired, or neglected, they will show their corresponding mood.
- **Inventory**: Your pet has a small inventory of items like kibble, treats, and fish. Use these items to keep them fed and happy.

## Saving and Loading

The game uses a `pet_save.json` file to save and load your pet’s progress. When you choose to save your game, the current state of your pet (including stats, tricks, inventory, and XP) will be saved to this file. If you want to load your pet's progress, the game will read from this file and restore your pet’s state.

---

## File Structure

Here’s a quick look at the file structure:

```
pet-time-adventures*/
├── pet_game.py      # Main game file
├── pet.py           # Pet class definition
└── pet_save.json    # Save file (created after saving progress)
```

## How to Play

Once the game starts, you’ll be prompted with a menu of actions:

1. **Feed your pet**: Feed your pet from the available inventory (e.g., kibble, treats, fish).
2. **Let your pet sleep**: Your pet will restore energy and health by sleeping.
3. **Play with your pet**: Your pet will play, and in return, they’ll become happier and hungrier.
4. **Train a trick**: Teach your pet a new trick.
5. **Show learned tricks**: Display the list of tricks your pet has learned.
6. **View pet status**: Check on your pet's current stats.
7. **Random events**: Encounter events that affect your pet's happiness or health.
8. **Quit the game**: Save the pet’s progress and exit the game.

## Game Over

The game ends when your pet’s happiness, hunger, or energy reaches critical levels, or if they become too neglected. If your pet runs away, the game will notify you, and you will need to start over.

---

## Contributing

If you want to contribute to **PetTime Adventures**, feel free to fork the repository and create a pull request with your improvements or bug fixes. We welcome suggestions for new features or ways to improve the pet care experience.

---

## License

This project is open source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Enjoy the game and have fun with your virtual pet! 🐾
