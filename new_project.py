# Investiční strategie na D1 grafu indexu S&P 500 využívající indikátory Williams %R, Momentum
# Podmínky pro nákup:
# Pokud je Williams %R s periodou 10 pod úrovni -90 a Momentum s periodou 25 je rostoucí

class Greetings:
    def __init__(self, separator, greetings):
        self.separator = separator
        self.greetings = greetings


    def create_greetings(self):
        print(f"{self.separator}\n{self.greetings}\n{self.separator}")


class Conditions:
    def __init__(self, separator, condition1, separator2, condition2):
        self.separator = separator
        self.condition1 = condition1
        self.separator2 = separator2
        self.condition2 = condition2


    def create_conditions(self):  
        if float(input(self.condition1)) < -90 and input(f"{self.separator2}\n{self.condition2}") == "ano":
            print(f"{self.separator}\nVýborně. Podmínky pro další nákup podílů ETF jsou splněny.")

        else:
            print(f"{self.separator}\nBohužel, dnes nejsou splněny podmínky pro další nákup. Užívej dne. Ahoj :-)\n")


my_greet = Greetings(75 * "=", "Ahoj, uživateli. Je čas vyhodnotit včerejší obchodní den indexu S&P 500" )
my_greet.create_greetings()

my_conditions = Conditions(
    75 * "=",  
    "Jaká je hodnota Williams %R(10):\n",
    75 * "-", 
    "Je Momentum rostoucí? Ano nebo ne.\n"
)
my_conditions.create_conditions()