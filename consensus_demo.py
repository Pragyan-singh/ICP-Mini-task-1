import random

# PoW: select highest power
pow_validators = [{"id": "A", "power": random.randint(1, 100)},
                  {"id": "B", "power": random.randint(1, 100)},
                  {"id": "C", "power": random.randint(1, 100)}]
pow_winner = max(pow_validators, key=lambda x: x['power'])
print(f"PoW Winner: {pow_winner['id']} (Power: {pow_winner['power']})")
print("-> Selected based on highest computational power\n")

# PoS: select highest stake
pos_validators = [{"id": "X", "stake": random.randint(1, 1000)},
                  {"id": "Y", "stake": random.randint(1, 1000)},
                  {"id": "Z", "stake": random.randint(1, 1000)}]
pos_winner = max(pos_validators, key=lambda x: x['stake'])
print(f"PoS Winner: {pos_winner['id']} (Stake: {pos_winner['stake']})")
print("-> Selected based on highest amount staked\n")

# DPoS: select by votes
delegates = ["Node1", "Node2", "Node3"]
votes = {"Alice": "Node2", "Bob": "Node2", "Charlie": "Node1"}

vote_count = {}
for vote in votes.values():
    vote_count[vote] = vote_count.get(vote, 0) + 1

dpos_winner = max(vote_count, key=vote_count.get)
print(f"DPoS Winner: {dpos_winner} (Votes: {vote_count[dpos_winner]})")
print("-> Selected based on most votes by token holders\n")
