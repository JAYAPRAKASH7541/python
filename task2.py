class Block:
    # TODO: write your code here
    def __init__(self,value):
        self._value=value
        
    def __str__(self):
        return "+{}+\n|{}|\n+{}+".format(('-'*len(str(block_value))),(block_value),('-'*len(str(block_value))))


if __name__ == "__main__":
    block_value = int(input())

    block_one = Block(block_value)

    print(block_one)
