class Block:
    # TODO: write your code here
    def __init__(self,value):
        self._value=value
    
    @property
    def value(self):
        return self._value
        
    
    


if __name__ == "__main__":
    import json
    input_args = json.loads(input())

    block_one = Block(input_args[0])
    block_two = Block(input_args[1])

    try:
        block_one._value
    except AttributeError:
        print("Missed protecting value")

    try:
        block_one.value = 1
        print("Missed setting safe access to value")
    except AttributeError:
        pass

    print(block_one.value)
