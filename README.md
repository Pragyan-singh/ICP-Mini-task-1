# ICP-Mini-task-1
Task 1 given in ICP internship
# 🧱 Mini Task 1: Build & Explain a Simple Blockchain

This project is a hands-on exercise to understand how a blockchain works by simulating its basic components and mechanisms using Python. It is divided into three code-based parts:

- ✅ Blockchain Structure Simulation
- ✅ Proof-of-Work (Mining)
- ✅ Consensus Mechanisms: PoW, PoS, and DPoS

---

## 📁 Files Included

| Filename                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `blockchain_simulation.py` | Simulates 3 connected blocks in a blockchain and demonstrates chain tampering |
| `mining_simulation.py`     | Simulates Proof-of-Work mining by finding a hash that satisfies difficulty   |
| `consensus_demo.py`        | Demonstrates PoW, PoS, and DPoS consensus logic with mock validators         |

---

## 🔹 Task 1: `blockchain_simulation.py` – Basic Blockchain Structure

### 🎯 Objective:
Create a minimal blockchain structure of 3 blocks, each storing:
- `index`
- `timestamp`
- `data`
- `previousHash`
- `hash`
- `nonce`

### 🛠️ What it does:
- Hashes are calculated using SHA-256
- Each block is linked to the previous via `previousHash`
- Demonstrates that tampering one block invalidates the rest

### 🖥️ Output Example:
Block #1
Data: Block 1 Data
Hash: d3a1f...

--- Tampering with Block 1 ---
Block #1
Data: Hacked Data
Hash: 9f82e...
Block #2
Data: Block 2 Data
Hash: INVALID (because its previous hash is outdated)


### 💡 Takeaway:
> Tampering with a block breaks the integrity of the entire chain — demonstrating immutability.

---

## 🔹 Task 2: `mining_simulation.py` – Proof-of-Work Mining

### 🎯 Objective:
Simulate mining by using a brute-force method to find a nonce that makes the block hash start with a certain number of zeroes (difficulty).

### 🛠️ What it does:
- Defines a `mineBlock()` function
- Increments the nonce until the hash matches the difficulty
- Measures number of attempts and time taken

### 🖥️ Output Example:
Block mined: 0000a84...
Nonce attempts: 52391
Time taken: 1.5320 seconds


### 💡 Takeaway:
> Proof-of-Work is computationally expensive. The higher the difficulty, the more resources required to mine a block.

---

## 🔹 Task 3: `consensus_demo.py` – Consensus Mechanisms (PoW, PoS, DPoS)

### 🎯 Objective:
Simulate three different consensus mechanisms:
- PoW: Proof-of-Work
- PoS: Proof-of-Stake
- DPoS: Delegated Proof-of-Stake

### 🛠️ What it does:
- Creates mock validators:
  - PoW → validators with random `power`
  - PoS → validators with random `stake`
  - DPoS → delegates voted by mock users
- Prints the selected validator and explains logic

### 🖥️ Output Example:
PoW Winner: B (Power: 98)
-> Selected based on highest computational power

PoS Winner: X (Stake: 765)
-> Selected based on highest amount staked

DPoS Winner: Node2 (Votes: 2)
-> Selected based on most community votes


### 💡 Takeaway:
> Consensus methods define how the next block producer is selected. Each has trade-offs in speed, decentralization, and fairness.

---

## 🧪 How to Run

Make sure Python 3 is installed. Then run:

```bash
python blockchain_simulation.py
python mining_simulation.py
python consensus_demo.py
