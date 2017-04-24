import sys
import random
import math

def random_list(min, max, no_elements) :
    list = random.sample(range(min, max), no_elements)
    return list

class Data :
    """ This class has 2 fields, KEY and LITERAL(Value) """
    def __init__(self, key) :
        self.key = key
        self.literal = str(key)

    def getKey(self) :
        return self.key

    def getLiteral(self) :
        return self.literal

class HashMap :
    """ This class has only array (1D array) """
    def __init__(self, size, option_main = 0, option_side = 0, c1 = 3, c2 = 2) :
        self.array = [None for i in range(0, size)]
        self.size = size
        self.option_main = option_main
        self.option_side = option_side
        self.c1 = c1
        self.c2 = c2

    """ Function to print whole array """
    def print_map(self) :
        for item in self.array :
            if(item != None) :
                print("[ Key: ", item.key, " Literal: ", item.literal, " ]")

    """ Side hash function """
    def _hash1(self, key) :
        if(self.option_side == 0) :
            return (key % self.size)
        if(self.option_side == 1) :
            return (1 + (key % (self.size - 1)))

    def _hash2(self, key) :
        if(self.option_side == 1) :
            return (key % self.size)
        if(self.option_side == 0) :
            return (1 + (key % (self.size - 1)))

    """ Hash function with side function h' """
    def _hash_function(self, key, i) :
        #0 - Linear probing
        if(self.option_main == 0) :
            return ((self._hash1(key) + i) % self.size)
        #1 - Quadratic probing
        if(self.option_main == 1) :
            return((self._hash1(key) + self.c1 * i + self.c2 * i * i) % self.size)
        #2 - Double hashing
        if(self.option_main == 2) :
            return((self._hash1(key) + self._hash2(key)) % self.size)

    """ Inserting function, tries to insert element
        to list, that slot is full then it tries to
        insert it to next slot according to _hash_function()
     """
    def insert(self, data) :
        i = 0
        while(1) :
            slot = self._hash_function(data.key, i)  

            if(self.array[slot] != None) :
                if(self.array[slot].key == data.key) : #if there is item with same key
                      self.array[slot] = data            #just update it's data
                      return True

            if (self.array[slot] == None) : # if that key is unique
                self.array[slot] = data     # inser that item in first available place
                return True                 # inside table 
                
            i += 1    
            if(i == self.size) :
                break

        print("Hash table is full")
        return False

    """ Searchin function
    """
    def search(self, key) :
        i = 0
        while(1) :
            slot = self._hash_function(key, i)
            
            if(self.array[slot] == None) : #No item at place where it should look next, so no that item
                break          
            
            if(self.array[slot].key == key) :
                return self.array[slot]

            i += 1

            if(i == self.size + 1) : #List full searched, no that item
                break

        print("Whole list searched, and no item found")
        return None
            
#Main

hashMap = HashMap(11,2)

list = random_list(0, 20, 10)


for i in range(0, len(list)) :
    data = Data(list[i])
    hashMap.insert(data)

print("Init list : ", list)
print()
hashMap.print_map()

key_for_search = list[5]
print("Searching for key : ", key_for_search, "...")
temp = hashMap.search(key_for_search)

if(temp != None) :
    print("Key found ", temp.key, " literal : ", temp.literal)
else :
    print("No key found")

key_for_search = 123
print("Searching for key : ", key_for_search, "...")
temp = hashMap.search(key_for_search)

if(temp != None) :
    print("Key found ", temp.key, " literal : ", temp.literal)
else :
    print("No key found")


print(hashMap.array)
    