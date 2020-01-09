print("Imported MyModule.py")

test = 'Test string'

def find_index(to_search, target):
    """find the index defined in target within the list to_search"""
    for i, value in enumerate(to_search):
        if value == target:
            return i
        return -1


