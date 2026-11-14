class Player:
    #constructor 
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role},{self.credits} cr)"


class FantasyTeam:
    def __inti__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.player = []
        self.captain = None
        self.vice_captain = None
    
    def add_player(self,player):
        self.players.append(player)
    
    def total_credits(self):
        total = 0
        for player in self.players:
            total = total + player.credits
        return total
    
    def count_by_role(self):
        counts = {
            "WK":0,
            "BAT":0,
            "AR":0,
            "BOWL":0
        }
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts


# def __str__(self):
#     return (
#         f"Player Id : {self.player_id}\n",
#         f"Player Name : {self.name}\n",
#         f"Player Role : {self.role}\n",
#         f"Franchise Name : {self.franchise}\n",
#         f"Player Credits : {self.credits}cr\n"
#     )
# object
babar = Player("P089", "Babar Azam", "Batter", "Peshawer Zalmi", 10.5)
# print (babar)
# info check krny k liya
# print(babar.name)
# print(babar.franchise)
# print(babar.credits)
rizwan = Player("P122", "Mohammad Rizwan", "Wk", "Rawal pindiz", 10.5)
# print(rizwan)
# class Player:
#     #constructor 
#     def __init__(self, player_id, name, role, franchise, credits):
#         self.player_id = player_id
#         self.name = name
#         self.role = role
#         self.franchise = franchise
#         self.credits = credits

#     def __str__(self):
#         return f"{self.name} ({self.franchise}, {self.role},{self.credits} cr)"


# print(FantasyTeam)
# def __str__(self):
#     return (
#         f"Player Id : {self.player_id}\n",
#         f"Player Name : {self.name}\n",
#         f"Player Role : {self.role}\n",
#         f"Franchise Name : {self.franchise}\n",
#         f"Player Credits : {self.credits}cr\n"
#     )
# object
# babar = Player("P089", "Babar Azam", "Batter", "Peshawer Zalmi", 10.5)
# print (babar)
# info check krny k liya
# print(babar.name)
# print(babar.franchise)
# print(babar.credits)
shaheen = Player("P068", "Shaheen Shah Afridi", "BOWL", "Lahore Qalandars", 10.5)
# print(shaheen)
fakhar = Player("P056", "Fakhar Zaman", "Batter", "Lahore Qalandars", 8.5)
# print(fakhar)
sameer = Player("P025", "Sameer Minhas", "Batter", "Islamabad United", 7.5)
# print(sameer)
haris = Player("P087", "Mohammad Haris", "WK", "Peshawar Zalmi", 7.5)
# print(haris)
for player in [babar,rizwan,fakhar,sameer,haris,shaheen]:
    print(player)