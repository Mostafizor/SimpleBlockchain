import hashlib as hs
import datetime as date

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
		print('Block Reward: 50 Coins.')

class Blockchain(object):
	def __init__(self):
		self.chain = [self.createGenesisBlock()]
		self.difficulty = 5

	def createGenesisBlock(self):
		return Block(0, str(date.datetime.now()), 'Genesis Block', '0')

	def getLatestBlock(self):
		return self.chain[len(self.chain) - 1]

	def nextBlock(self, lastBlock):
		index = lastBlock.index + 1
		timestamp = str(date.datetime.now())
		previousHash = lastBlock.calculateHash()
		data = '200 Coins'
		return Block(index, timestamp, data, previousHash)

	def addBlock(self, newBlock):
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

# Create Blockchain
coin = Blockchain()

num_blocks = int(raw_input('How many blocks would you like to mine? > '))
for i in range(num_blocks):
	coin.addBlock(coin.nextBlock(coin.getLatestBlock()))

# Check if Blockchain is valid
print('Is Chain Valid ?: %s' %(coin.isChainValid()))

# Print Block Chain Data
for b in range(len(coin.chain)):
	print('Block: %s' %(b), vars(coin.chain[b]))
	print('')
