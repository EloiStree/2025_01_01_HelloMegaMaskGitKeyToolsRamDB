

# Hello MegaMask Git Key Tools Ram DB

A toolbox designed to run on a Raspberry Pi that provides "ram database access" and functionality using a Git-based index claim.

## Concept
The idea is simple:  
You can claim a number between `0` and `2,147,483,647`.

The administrator only needs to add your public key to the folder of the claimed index.

Inside this toolbox, you will find tools that enable interaction with the claims.

### Examples:
1. **Flask API**:  
   - Reads the values stored in RAM when loaded and provides API access to them.

2. **Gathering Script**:  
   - A Python script that runs every N seconds as a service, merging information into a single file.

#### Example Usage:
`/42/0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A`

- The folder `42` is owned by `0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A`.

If a user wants to modify the claim, they must provide a signed message using:  
`0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A`.  

If they fail to do so, their request will be denied.  
"Own the key, own the index."

I’m considering writing some code that allows a signed message to securely exchange ownership of the index.  
However, if you trust the buyer, you can simply provide them with the private key and let them replace it with their own key directly to take ownership.


### Note:

- A user is around 46 characters in a file.
- To reach the maximum number of users, you would need **98,784,247,762 bytes** (about **92 GB**) of RAM.

Given that:

- **Pi** has 4 GB of RAM, with 2 GB already used by other processes, leaving 2 GB for user data.
- With **2 GB of available RAM**, you can store around **46,684,427 users** .

If you reach this amount, it might be time to consider a **rework** of the system 😅.

_Suggestion:_ Try to keep it to a maximum of 1 million users for now (^^').








