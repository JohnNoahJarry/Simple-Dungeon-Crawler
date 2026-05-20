# Simple-Dungeon-Crawler

A simple terminal game where you go through a dungeon and fight enemies.

## Version 1.0.0 Changelog

- Initial Version of the Game Uploaded.

## Summary

This terminal game has you exploring a dungeon of 10 floors.

As you go through the dungeon, you'll be encountering enemies which you can either fight or run away from. Fight and win to gain Gold and Experience Points, or run away if the odds look rough, though you will not gain any Gold or XP for doing so. The maximum Gold you can carry is 1000, while the maximum level you can reach is 100.

Each floor contains a Rest Area to heal your wounds, a Shop to spend your gold on items or new party members, an Item Room with a free item choice among 3 items, and the Exit to the next floor.

At the top of the screen is a value called "Moves Left". It determines how long you have left to stay on a floor before the game forces you to the next floor.

There are 4 main stats in the game that increase a unit levels up. HP is how much damage a unit can take before the unit becomes defeated. ATK is how much damage a unit does per attack. DEF is how much damage a unit randomly blocks as they get hit with an attack. SPD detemines who acts first in a battle. SPD also affects your Flee chance, the higher your SPD stat is compared to the enemies' SPD stats, the better your fleeing odds.

There are 4 types of equipment in the game. Helmets increase a unit's HP by 20 per level. Swords increase a unit's ATK by 20 per level. Armor increases a unit's DEF by 20 per level. Boots increase a unit's SPD by 20 per level.

At the final floor, the Exit will be replaced with a Boss Room to fight the final boss. If you run out of moves on the final floor, you will automatically start a battle with the final boss. Defeat them to win the game!

## Requirements

This project was created using Python 3.12.3. It is recommended to use this version or higher.

## Credits

This project uses the proper name database of ENAMDICT/JMnedict (https://www.edrdg.org/enamdict/enamdict_doc.html) to generate names for the units in-game.
