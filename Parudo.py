import random

class player: #why didn't we need (object)?
    def __init__(self, name):
        self.name = name
        self.dice = [0] * 6
        self.types = [0] * 6
    
    def dice_num(self):
        return len(self.dice)
    
    def roll(self, total_types=None): #make total_types variable
        for die in self.dice:
            die = random.randint(1,6)
            self.types[die-1] += 1
            if total_types:
                total_types[die-1] += 1

    def guess(self, total_dice, kind, number): # make better, maybe change returns
        call = False
        if random.randint(0,5) == 0:
            call = True
            return (call, kind, number)
        kind = random.randint(kind,6)
        number = random.randint(max(player.types[kind-1], number), total_dice) #
        return (call, kind, number)

    def lose_die(self):
        self.dice.pop()
        if not self.dice: # no dice
            return True
        else:
            return False
    
if __name__ == "__main__":
    num_players = 6 # parameter
    players = [player("{:08}".format(random.randint(0,99999999))) for i in range(num_players)]
    
    while len(players) > 1:
        total_types = [0] * 6
        for (index, player) in enumerate(players):
            player.roll(total_types)
            total_dice = sum(total_types)

        kind = 1
        number = 0
        call = False
        while not call:
            for (index, player) in enumerate(players):
                (call, kind, number) = player.guess(total_dice, kind, number)
                if call:
                    if total_types[kind-1] >= number:
                        if player.lose_die():
                            del players[index]
                        print("{} loses a die".format(players[index].name))
                    else:
                        if players[index-1].lose_die():
                            del players[index-1]
                        print("{} loses a die".format(players[index-1].name))
                        
                else:
                    print("{} guesses {} of type {}".format(player.name, number, kind))
