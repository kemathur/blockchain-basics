import hashlib


class MerkleTree:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def getSHA2HexValue(self, source):
        hash_object = hashlib.sha256(source.encode())
        digest = hash_object.hexdigest()
        return digest
    
    def getHash(self, source):
        return '('+ source + ')' +'*'
        # return self.getSHA2HexValue(source)

    # 0 1 2 3
    # 0 1 2
    # i < n - 1
    def getNextMerkleRow(self, input):
        ret = []
        n = len(input)
        if n == 0:
            return ret
        i=0
        while i < n-1:
            concat = input[i] + input[i+1]
            hashX = self.getHash(concat)
            ret.append(hashX)
            i += 2
        if i == n-1:
            ret.append(self.getHash(input[i] + input[i]))
        print (ret)
        return ret

    def getMerkleRoot(self, transactions):
        if transactions == None or len(transactions) == 0:
            return None

        nextRow = self.getNextMerkleRow(transactions)
        if (len(nextRow) == 1):
            return nextRow[0]

        return self.getMerkleRoot(nextRow)

if __name__ == "__main__":
    trx = ['a', 'b', 'c', 'd', 'e']
    mkt = MerkleTree()
    print (mkt.getMerkleRoot(trx))