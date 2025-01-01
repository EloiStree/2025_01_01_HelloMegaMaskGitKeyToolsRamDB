

# 2025_01_01_HelloMegaMaskGitKeyToolsRamDB

A toolbox designed to run on a Raspberry Pi that provides database access and functionality using a Git-based index claim.

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

