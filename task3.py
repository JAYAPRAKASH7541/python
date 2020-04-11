class Block:
    # TODO: write your code here
    def __init__(self,value):
        self._value=value
        
    def __add__(self,other):
        if self._value == other._value:
            return Block(self._value+other._value)
        else:
            print("Cannot add blocks with different values")


if __name__ == "__main__":
    import json

    input_args = json.loads(input())

    block_one = Block(input_args[0])
    block_two = Block(input_args[1])

    block_result = block_one + block_two

    print(isinstance(block_result, Block))
    if isinstance(block_result, Block):
        print(block_result._value)
