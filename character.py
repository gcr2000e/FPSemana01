character_name1 = input()
character_name2 = input()
character_name3 = input()

attack1 = input()
attack2 = input()
attack3 = input()

defense1 = input()
defense2 = input()
defense3 = input()

char = [
    [(character_name1), (attack1), (defense1)],
    [(character_name2), (attack2), (defense2)],
    [(character_name3), (attack3), (defense3)]
]

print(
    char[0][0],
    char[0][1],
    char[0][2],

    char[1][0],
    char[1][1],
    char[1][2],

    char[2][0],
    char[2][1],
    char[2][2]
)