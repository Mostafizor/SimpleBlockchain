import hashlib as hs

class Block(object):
	def __init__(self, index, timestamp, data, previousHash = ''):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previousHash = previousHash
		self.hash = self.calculateHash()

	def calculateHash(self):
		return hs.sha256(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousHash)).hexdigest()

class Blockchain(object):
	def __init__(self):
		self.chain = [self.createGenesisBlock()]

	def createGenesisBlock(self):
		return Block('0', '25/09/2017', 'Genesis Block', '0')

	def getLatestBlock(self):
		return self.chain[len(self.chain) - 1]

	def addBlock(self, newBlock):
		newBlock.previousHash = self.getLatestBlock().hash
		newBlock.hash = newBlock.calculateHash()
		self.chain.append(newBlock)

	def isChainValid(self):
		for i in range(1, len(self.chain)):
			currentBlock = self.chain[i]
			previousBlock = self.chain[i-1]

			if currentBlock.hash != currentBlock.calculateHash():
				return False
			elif currentBlock.previousHash != previousBlock.hash:
				return False
		return True

# Create Blocks(Transactions)
coin = Blockchain()
coin.addBlock(Block('1', '25/09/2017', 'Mo sent 5 coins to Satoshi'))
coin.addBlock(Block('2', '25/09/2017', 'Satoshi sent 20 coins to Mo'))
coin.addBlock(Block('3', '25/09/2017', 'Satoshi sent 2000 coins to Mo'))

# Check if Blockchain is valid
print('Is Chain Valid ?: %s' %(coin.isChainValid()))

# Print Block Chain Data
for b in range(len(coin.chain)):
	print('Block: %s' %(b), vars(coin.chain[b]))
	print('')

# Tamper with the Blockchain
coin.chain[2].data = 'Satoshi sent 50000 coins to Mo'
coin.chain[2].hash = coin.chain[2].calculateHash()

# Check validity of Blockchain after tampering
print('Is Chain Valid ?: %s' %(coin.isChainValid()))

# Print tampered Blockchain data
for b in range(len(coin.chain)):
	print('Block: %s' %(b), vars(coin.chain[b]))
	print('')
