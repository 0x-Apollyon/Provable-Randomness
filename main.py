square_size = 3
number_of_mines = 1
number_of_tiles = square_size*square_size
number_of_gems = number_of_tiles - number_of_mines

if number_of_tiles < number_of_mines:
    print("Number of tiles cant be less than number of mines")
    quit()

game_layout = []

for i in range(number_of_mines):
    game_layout.append(1)

for i in range(number_of_gems):
    game_layout.append(0)

import random
import os
import hashlib

server_seed = hashlib.sha256(os.urandom(32)).hexdigest()
server_seed_hashed = hashlib.sha256(server_seed.encode()).hexdigest()

print(f"The current server seed hash is {server_seed_hashed}")
client_seed = input("Enter client seed: ").strip()
client_seed_hashed = hashlib.sha256(client_seed.encode()).hexdigest()

final_seed = client_seed_hashed +  server_seed

random.seed(final_seed)
random.shuffle(game_layout)

square_layout = []

square_row = []
for j , i in enumerate(game_layout):
    square_row.append(i)
    if (j+1)%square_size == 0:
        square_layout.append(square_row)
        square_row = []

mine_struck = False 

game_state = []
for i in range(square_size):
    row = []
    for j in range(square_size):
        row.append(0)
    game_state.append(row)
    row = []

while not mine_struck:
    print("\n")
    for i , row in enumerate(square_layout):
        for j , element in enumerate(row):
            if game_state[i][j] == 0:
                print(f"  [{i+1} , {j+1}]  " , end = "")
            else:
                print("     *     " , end = "")
        print("")
    print("\n")
    coords = input("Select the tile with its numbers split with a comma or quit to end the game: ").strip()
    if coords != "quit":
        coords = coords.split(",")

        
        first_coord = int(coords[0])
        second_coord = int(coords[1])

        if square_layout[first_coord-1][second_coord-1] == 1:
            print("You hit the mine. BOOM !!")
            print(f"Client seed for verification: {server_seed}")
            mine_struck = True
        else:
            game_state[first_coord-1][second_coord-1] = 1
    else:
        print("Game ended")
        print(f"Server seed for verification: {server_seed}")
        mine_struck = True