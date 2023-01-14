from random import randint
 
 
def main():
    choices = {1: "Piatra", 2: "Hartie", 3: "Foarfece"}
    scor = 0
    incercari = 0
 
    while True:
 
        try:
            choices = int(input("\n1. Piatra, 2. Hartie, 3. Foarfece, 4. Exit: "))
 
            if your_choice == 4:
                break
            if your_choice not in {1, 2, 3}:
                incercari -= (
                    1  
                )
 
            computer_choice = randint(1, 3)
            incercari += 1
            print(
                f"Ai ales {choices[your_choice]} iar computerul a ales {choices[computer_choice]}"
            )
 
            if your_choice == computer_choice:
                print("Remiza.")
                incercari -= 1
            elif str(your_choice) + str(computer_choice) in ["13", "21", "32"]:
                print("Ai castigat!")
                scor += 1
            else:
                print("Ai pierdut. :((")
        except:
            print("Alegere invalida.")
            break
 
    print(f"Scorul tau este {scor}/{incercari}")
 
 
main()
