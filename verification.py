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

import hashlib
import random

client_input = input("What was the client input: ").strip()
server_seed = input("What was the final revealed server seed: ").strip()
server_seed_hash = input("What was the initially revealed server seed hash: ").strip()


client_input_hashed = hashlib.sha256(client_input.encode()).hexdigest()
final_seed = client_input_hashed + server_seed

if hashlib.sha256(server_seed.encode()).hexdigest() == server_seed_hash:
    print("Server Seed Hash verified. The game was provably fair.")
else:
    print("Server Seed Hash verification failed, the game wasnt fair.")

random.seed(final_seed)
random.shuffle(game_layout)

for j , i in enumerate(game_layout):

    if i == 0:
        print("   GEM   ", end="")
    else:
        print("   MINE  " , end="")

    if (j+1)%square_size == 0:
        print()