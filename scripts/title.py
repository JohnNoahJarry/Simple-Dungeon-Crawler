import scripts.characterCreator, scripts.dungeon
import ui.general, ui.title

def main():
  while True:
    ui.general.clearScreen()
    ui.title.displayTitleScreen()
    choice = ui.general.displayUserInput()

    if choice == "1":
      system = scripts.characterCreator.main()
      scripts.dungeon.main(system)
    elif choice == "2":
      break