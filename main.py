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
    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
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
    
    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain
    
    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name}(owner: {self.owner},{size} player, {cost} cr)"

team = FantasyTeam("Dugout Demo XI", "Waqar")



babar = Player("P089", "Babar Azam", "BAT", "Peshawar Zalmi", 10.5)# Batsmen
rizwan = Player("P122", "Mohammad Rizwan", "WK", "Rawalpindiz", 10.5) # Wicket Keepers
fakhar = Player("P056", "Fakhar Zaman", "BAT", "Lahore Qalandars", 8.5)# Batsmen
sameer = Player("P025", "Sameer Minhas", "BAT", "Islamabad United", 7.5)# Batsmen
haris = Player("P087", "Mohammad Haris", "WK", "Peshawar Zalmi", 7.5)# Wicket Keepers
# All-Rounders
saim = Player("P012", "Saim Ayub", "AR", "Hyderabad Kingsmen", 10.5)
arafat = Player("P077", "Arafat Minhas", "AR", "Multan Sultans", 7.0)
faheem = Player("P027", "Faheem Ashraf", "AR", "Islamabad United", 9.5)

# Bowlers
shaheen = Player("P068", "Shaheen Shah Afridi", "BOWL", "Lahore Qalandars", 10.5)
haris_rauf = Player("P066", "Haris Rauf", "BOWL", "Lahore Qalandars", 7.5)
amir = Player("P137", "Mohammad Amir", "BOWL", "Rawalpindiz", 8.5)

# All 11 Players
for player in [
    babar, rizwan, fakhar, sameer,
    haris, shaheen, saim, arafat,
    faheem, haris_rauf, amir
]:
    team.add_player(player)
team.set_captain(babar,rizwan)

print(team)
print("Roles:",team.count_by_role())
print("Captain:", team.captain)
print("Vice-captain:", team.vice_captain)

"""
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
fakhar = Player("P056", "Fakhar Zaman", "BAT", "Lahore Qalandars", 8.5)
# print(fakhar)
sameer = Player("P025", "Sameer Minhas", "BAT", "Islamabad United", 7.5)
# print(sameer)
haris = Player("P087", "Mohammad Haris", "WK", "Peshawar Zalmi", 7.5)
# print(haris)
for player in [babar,rizwan,fakhar,sameer,haris,shaheen]:
    print(player)
"""