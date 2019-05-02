import hashlib
import time

class Block:
    count = 0
    def __init__(self, prevHash, trx):
        self.prevHash = prevHash
        self.trx = trx
        self.ts = time.time_ns()
        self.blockHeight = Block.count
        # self.currentHash = self.computeHash()
        self.difficulty = 2
        self.nonce = self.computeNonce()
        Block.count += 1

    @staticmethod
    def getSHA2HexValue(source):
        hash_object = hashlib.sha256(source.encode())
        digest = hash_object.hexdigest()
        return digest

    @staticmethod
    def create_hash(source):
        # return '('+ source + ')' +'*'
        return Block.getSHA2HexValue(source)

    def createHeader(self):
        header = self.prevHash + str(self.ts)
        trxString = ""
        for t in self.trx:
            trxString += t
        header += Block.create_hash(trxString)
        return header

    # Basically mine the block
    def computeNonce(self):
        nonce = 0
        hashX = "x"
        header = self.createHeader()
        while hashX[:self.difficulty] != '0'*self.difficulty:
            nonce += 1
            x = header + str(nonce)
            hashX = Block.create_hash(x)
        print(hashX)
        print ("======== :: nonce :: " , nonce)
        return nonce

    def computeHash(self):
        return '0000' + Block.create_hash(self.createHeader())

    def getPrevHash(self):
        return self.prevHash

    def getTrx(self):
        return self.trx

    def getTs(self):
        return self.ts

    def getBlockHeight(self):
        return self.blockHeight
    
    def getCurrentHash(self):
        return Block.create_hash(self.createHeader() + str(self.nonce))

    def getDifficulty(self):
        return self.difficulty


def isChainValid(blockChain):
    for b in blockChain:
        difficulty = b.getDifficulty()
        bHash = b.getCurrentHash()
        if bHash[:difficulty] != '0'*difficulty:
            return False
    return True


if __name__ == "__main__":
    blockChain = []
    blockChain.append(Block("", ['a', 'b']))
    blockChain.append(Block(blockChain[0].getCurrentHash(), ['c', 'd']))

    for b in blockChain:
        print (b.getBlockHeight(), b.getCurrentHash())
    print (isChainValid(blockChain))

