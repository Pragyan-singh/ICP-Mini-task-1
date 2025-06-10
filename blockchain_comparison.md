
# Blockchain Platform Comparison

## 📊 Comparison Table

| Blockchain Name     | Type         | Consensus Mechanism       | Permission Model | Speed / Throughput | Smart Contract Support     | Token Support     | Typical Use Case                   | Notable Technical Feature        |
|---------------------|--------------|----------------------------|------------------|--------------------|-----------------------------|-------------------|------------------------------------|----------------------------------|
| **Ethereum**        | Public       | Proof of Stake (Ethereum 2.0) | Open             | ~15–30 TPS (L1)    | Yes (Solidity, Vyper)       | Native (ETH)      | DApps, DeFi, NFTs                 | EVM compatibility, Layer-2 rollups |
| **Hyperledger Fabric** | Private   | Pluggable (e.g., Raft, Kafka) | Permissioned      | 1000+ TPS          | Yes (Chaincode in Go, Java, JavaScript) | No Native Token   | Enterprise supply chain, finance | Channel-based privacy model      |
| **R3 Corda**        | Consortium   | Notary-based (no global consensus) | Permissioned      | ~170 TPS (varies) | Yes (JVM-based; Kotlin, Java) | No Native Token   | Interbank settlements, KYC       | Point-to-point architecture       |

## 📝 Short Comparative Report

Ethereum, as a public blockchain, offers decentralized trust and robust smart contract functionality via the Ethereum Virtual Machine (EVM). However, it suffers from scalability issues on Layer 1 with relatively low throughput (~15–30 TPS), though Layer-2 solutions like rollups mitigate this.

Hyperledger Fabric is optimized for private enterprise use with high throughput and a modular consensus design. It supports private data channels and allows for fine-grained access control. However, it lacks a native token and is not ideal for open, decentralized systems.

R3 Corda, while consortium-oriented, blurs lines with private chains. It uses a unique point-to-point model, removing the need for global consensus. It's efficient and privacy-focused, ideal for inter-bank operations. Its smart contract model is based on legal prose and JVM-compatible languages.

### Platform Recommendations

- **Decentralized App (DApp):** *Ethereum* — due to its public nature, token economy, and developer ecosystem.
- **Supply Chain (known partners):** *Hyperledger Fabric* — because of high throughput, privacy channels, and pluggable consensus.
- **Inter-bank Finance:** *R3 Corda* — optimal for financial applications with privacy, legal contract integration, and efficient peer-to-peer communication.
