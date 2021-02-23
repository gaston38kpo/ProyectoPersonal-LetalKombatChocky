import time
import numpy as np
import sys

# Delay printing

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)

class Player:
    def __init__(self, name, stats):
        self.name = name
        self.minDMG = stats['MinDMG']
        self.maxDMG = stats['MaxDMG']
        self.armor = stats['ARMOR']
        self.health = stats['HEALTH']

    def damageCalculator(self, minDMG, maxDMG, armor):
        self.dmg = np.random.randint(minDMG, maxDMG)
        self.hit = round(self.dmg - self.dmg * armor / 100)
        return self.hit

    def fight(self, Player2):
        print('\n            FIGHT!')
        print('_______________________________')
        print(f'STATS  | {self.name}\tVS\t{Player2.name}')
        print('-------|-----------------------')
        print(f'DMG    | {self.minDMG}~{self.maxDMG}\t--\t{Player2.minDMG}~{Player2.maxDMG}')
        print(f'ARMOR  | {self.armor}\t--\t{Player2.armor}')
        print(f'HEALTH | {self.health}\t--\t{Player2.health}')
        print('-------------------------------')
              
        time.sleep(1.5)

        print("\n......Stats de vida.........")
        print(f"{self.name}\t\tHLTH\t{self.health}")
        print(f"{Player2.name}\t\tHLTH\t{Player2.health}")
        print("............................\n\n\n")

        time.sleep(.8)


        while (self.health > 0) and (Player2.health > 0):
            
            # ========= P1 turn =========
            print(f"\n\n\t\tVamos {self.name}!")

            # \\\\\\\\\ P healts  \\\\\\\\\

            time.sleep(.4)
            print("\t==============================")
            print(f"\t{self.name}\t\tHLTH\t{self.health}")
            print(f"\t{Player2.name}\t\tHLTH\t {Player2.health}    <=VS")            
            print("\t==============================")
            time.sleep(1.2)

            # \\\\\\\\\ Damage P1 calculator \\\\\\\\\ 

            self.damageCalculator(self.minDMG, self.maxDMG, Player2.armor)

            # \\\\\\\\\ Healt P2 calculator \\\\\\\\\

            Player2.health -= self.hit

            delay_print(f'''=============================================
{self.name} le ha inflingido {self.hit} de daño a {Player2.name}
=============================================
            ''')
            
            # \\\\\\\\\ Checking life P2 \\\\\\\\\
       
            if Player2.health <= 0:
                print(f"\n\t\t...{Player2.name} ha muerto.\n\t\t{self.name} es el ganador!\n")
                break


            # ========= P2 turn =========            
            print(f"\n\n\t\tVamos {Player2.name}!")   

            # \\\\\\\\\ P healts  \\\\\\\\\

            time.sleep(.4)
            
            print("\t==============================")
            print(f"\t{self.name}\t\tHLTH\t {self.health}    <=VS")
            print(f"\t{Player2.name}\t\tHLTH\t{Player2.health}")
            print("\t==============================")
            time.sleep(1.2)

            # \\\\\\\\\ Damage P2 calculator \\\\\\\\\

            Player2.damageCalculator(Player2.minDMG, Player2.maxDMG, self.armor)

            # \\\\\\\\\ Healt P1 calculator \\\\\\\\\

            self.health -= Player2.hit

            delay_print(f'''=============================================
{Player2.name} le ha inflingido {Player2.hit} de daño a {self.name}
=============================================
            ''')
            
            # \\\\\\\\\ Checking life P1 \\\\\\\\\

            if self.health <= 0:
                delay_print(f"\n\t\t...{self.name} ha muerto.\n\t\t{Player2.name} es el ganador!")
                break

            

if __name__ == '__main__':

    # All usage players add/modify manually

    freak = Player("Freak", {'MinDMG': 10, "MaxDMG": 15, "ARMOR": 10, "HEALTH": 25})
    chocky = Player("Chocky", {'MinDMG': 10, "MaxDMG": 15, "ARMOR": 10, "HEALTH": 25})
    garen = Player("Garen", {'MinDMG': 10, "MaxDMG": 15, "ARMOR": 10, "HEALTH": 25})
    jax = Player("Jax", {'MinDMG': 10, "MaxDMG": 15, "ARMOR": 10, "HEALTH": 25})
    ashe = Player("Ashe", {'MinDMG': 10, "MaxDMG": 15, "ARMOR": 10, "HEALTH": 25})
    lucian = Player("Lucian", {'MinDMG': 10, "MaxDMG": 15, "ARMOR": 10, "HEALTH": 25})
    

    # List of all usage players add/modify manually

    players = [freak, chocky, garen, jax, ashe, lucian]


    # Random player selection

    rIndex = np.random.randint(len(players))
    rIndex2 = np.random.randint(len(players))
    rPlayer = players[rIndex]
    rPlayer2 = players[rIndex2]


    # For manual/random player selection quote/unquote the following code:

    rPlayer.fight(rPlayer2)

    # And unquote/quote the following code:

    # freak.fight(chocky)
