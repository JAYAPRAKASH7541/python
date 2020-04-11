class Block:
    # TODO: write your code here
    def __init__(self,v):
        self._value=v
        
    @property
    def value(self):
        return self._value


class SuperBlock(Block):
    def split(self):
        if self.value==1:
            return ["+{}+\n|{}|\n+{}+".format('-'*len(str(self.value)),(self.value),'-'*len(str(self.value)))]
            
        elif self.value % 2==0:
            return ["+{}+\n|{}|\n+{}+".format('-'*len(str(self.value//2)),(self.value//2),'-'*len(str(self.value//2))),"+{}+\n|{}|\n+{}+".format('-'*len(str(self.value//2)),(self.value//2),'-'*len(str(self.value//2)))]
        else:
            return ["+{}+\n|{}|\n+{}+".format('-'*len(str((self.value-1)//2)),((self.value-1)//2),'-'*len(str((self.value-1)//2))),"+{}+\n|{}|\n+{}+".format('-'*len(str((self.value+1)//2)),((self.value+1)//2),'-'*len(str((self.value+1)//2)))]
            
        


if __name__ == "__main__":
    super_block_value = int(input())

    super_block_one = SuperBlock(super_block_value)

    try:
        super_block_one._value
    except AttributeError:
        print("Missed protecting value")

    try:
        super_block_one.value = 1
        print("Missed setting safe access to value")
    except AttributeError:
        pass

    print(isinstance(super_block_one, SuperBlock))

    try:
        print(isinstance(super_block_one, Block))
    except:
        print("You should use Block class to build SuperBlock")

    blocks = super_block_one.split()
    if len(blocks) > 1:
        print(blocks[0])
        print(blocks[1])
    else:
        print(blocks[0])
