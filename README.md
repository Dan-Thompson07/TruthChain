# TruthChain
TruthChain is a decentralized platform that uses AI to detect fake news and Algernon smart contracts to record verification results on the blockchain - ensuring transparency, accuracy, and trust in digital information

Insert demo video and screen shots here

# 📃Contract 1: NFT Minter & Creator 
 **Purpose:**
Creates an NFT via an inner transaction 

**Security**
- The use of IPFS for metadata storage, along with the inclusion of a metadata hash in the asset parameters, helps ensure the integrity and immutability of the NFT’s metadata
- The contract ensures that only the correct party (typically the contract itself or a designated manager) can mint the NFT.

 
# 👮 Key Security Features
- **SHA-256 Hash stored on clockchain for article integrity**:
  Provides proof of authenticity without having to store the article itself

- **Immutable Storage of results on the Algernon Blockchain**:
  AI results are written to the blockchain using Algernon smart contracts, which guarantees that verification results stay permanent and trustworthy.
-  **Data Privacy Through Off-Chain Storage**:
  The full article text and AI analysis are stored off-chain, meaning that Users’ data stays private while still verifiable via the hash.


# System interaction flow

**1.** User submits article text through the frontend.

**2.** Frontend sends the content to the backend AI module.

**3.** AI model analyzes the article using a pre-trained fake news detection algorithm and generates a Reliability Score.

**4.** Backend creates a SHA-256 hash of the article content to generate a unique digital fingerprint.

**5.** Backend calls the Algernon Smart Contract to record the hash, Reliability Score, and timestamp on the blockchain.

**6.** Blockchain transaction confirms the record, ensuring immutability and public verifiability.

**7.** Frontend displays results to the user — including the Reliability Score and the blockchain verification hash for transparency.

# ✅ Final Summary
TruthChain secures its AI verification process using SHA-256 hashing and Algernon smart contracts, ensuring that every news article’s integrity and authenticity can be independently verified, permanently stored, and protected from tampering.

The pre-made AI model is referenced here:
 https://github.com/kapilsinghnegi/Fake-News-Detection/tree/main
   
   Made by Kapil Singh Negi
   
   The model was modified for our project's needs
#

 **This architecture ensures that**:
- Every article’s fingerprint is securely hashed and immutably stored on-chain.
- Verification data remains tamper-proof and publicly auditable.
- AI models can evolve independently while maintaining historical integrity.
- Users can trust that no verified record can ever be altered or forged.

#
Blocklink:

 Presentation slides: https://www.canva.com/design/DAG2JagpovE/NmgKOyeF5YRgclb5q5H4Og/edit?utm_content=DAG2JagpovE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

