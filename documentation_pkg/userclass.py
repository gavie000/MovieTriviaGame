class User:
    def __init__(self, name):
        self.name = name

    def change_name(self,name):
        self.name = name
        print(self.name)

class Players(User):
    def __init__(self, name): 
        super().__init__(name)
        self.balance = 0

    def display_score(self):
       print(self.name,"has a score of" , self.balance)

    def display_name(self):
        answer = input( self.name, 'select and option: ')
        print(answer)

    # def change_score(self,amount):
    #      # maybe put input here. 
    #      # if the option to the question is correct then 
    #      # change the total balance of the players score
         
    #      if option == correct:
    #          self.balance += self.amount
    #          print("Yay!",self.name, "has a score of", self.balance)

    """Driver Test"""
# player1 = Players("Gaby")
# player2 = Players("Adolfo")
# player1.display_score()
# player2.display_score()
