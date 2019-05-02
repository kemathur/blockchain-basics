import hashlib
import time

class Block:
    count = 0
    def __init__(self, prevHash, trx):
        self.prevHash = prevHash
        self.trx = trx
        self.ts = time.time_ns()
        self.blockHeight = Block.count
        self.currentHash = self.computeHash()
        self.difficulty = 4
        Block.count += 1

    @staticmethod
    def getSHA2HexValue(source):
        hash_object = hashlib.sha256(source.encode())
        digest = hash_object.hexdigest()
        return digest

    @staticmethod
    def create_hash(source):
        return '('+ source + ')' +'*'
        # return getSHA2HexValue(source)

    def createHeader(self):
        header = self.prevHash + str(self.ts)
        trxString = ""
        for t in self.trx:
            trxString += t
        header += Block.create_hash(trxString)
        return header

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
        return self.currentHash

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