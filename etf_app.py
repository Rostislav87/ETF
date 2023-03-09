import sys


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
            sys.exit()


class Price:
    def __init__(self, actual_price, be_price, separator):
        self.actual_price = actual_price
        self.be_price = be_price
        self.separator = separator


    def price_setup(self):
        if float(input(self.actual_price)) > float(input(f"{self.separator}\n{self.be_price}")):
            print(f"{self.separator}\nAktuální cena je vyšší než tvoje průměrná nákupní cena.\nV tomto případě nakup 10 ks za market.\n")

        else: 
            print(f"{self.separator}\nAktuální cena je nižší než tvoje průměrná nákupní cena.\nV tomto případě nakup 20 ks za market.\n")


my_greet = Greetings(75 * "=", "Ahoj, uživateli. Je čas vyhodnotit včerejší obchodní den indexu S&P 500" )
my_conditions = Conditions(
    75 * "=",  
    "Jaká je hodnota Williams %R(10):\n",
    75 * "-", 
    "Je Momentum rostoucí? Ano nebo ne.\n"
)
my_price = Price("Jaká je aktuální cena ETF v EUR?\n", "Jaká je tvoje hrubá vážená průměrná cena nákupu tvé aktuální pozice?\n", 75 * "-")
my_greet.create_greetings()
my_conditions.create_conditions()
my_price.price_setup()