import hashlib as hs

class Block(object):
	def __init__(self, index, timestamp, data, previousHash = ''):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previousHash = previousHash
		self.nonce = 0
		self.hash = self.calculateHash()

	def calculateHash(self):
		return hs.sha256(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousHash) + str(self.nonce)).hexdigest()
							 
	def mineBlock(self, difficulty):
		print('Mining...')
		while self.hash[0:difficulty] != ''.join(['0'] * difficulty):
			self.nonce += 1
			self.hash = self.calculateHash()
		print('Block Mined: %s' %(self.hash))
		print('Block Reward: 50 Coins')
							
class Blockchain(object):
	def __init__(self):
		self.chain = [self.createGenesisBlock()]
		self.difficulty = 4

	def createGenesisBlock(self):
		return Block('0', '25/09/2017', 'Genesis Block', '0')

	def getLatestBlock(self):
		return self.chain[len(self.chain) - 1]

	def addBlock(self, newBlock):
		newBlock.previousHash = self.getLatestBlock().hash
		newBlock.mineBlock(self.difficulty)
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

num_blocks = int(raw_input('How Many Blocks Would You Like to Mine? >'))
for i in range(num_blocks/5):
	coin.addBlock(Block('1', '25/09/2017', 'Mo sent 5 coins to Satoshi'))
	coin.addBlock(Block('2', '25/09/2017', 'Satoshi sent 20 coins to Mo'))
	coin.addBlock(Block('3', '25/09/2017', 'Satoshi sent 2000 coins to Mo'))
	coin.addBlock(Block('4', '08/10/2017', 'Tohseef sent 5000 coins to Hammy'))
	coin.addBlock(Block('5', '08/10/2017', 'Mo sent 10000 coins to Satoshi'))

# Check if Blockchain is valid
print('Is Chain Valid ?: %s' %(coin.isChainValid()))

# Print Block Chain Data
for b in range(len(coin.chain)):
	print('Block: %s' %(b), vars(coin.chain[b]))
	print('')
