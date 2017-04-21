import sys
import math
import random

KNUTH = (math.sqrt(5) - 1) / 2

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
    """ This class has array as field """
    def __init__(self, size, option, p = 23) :
        self.array = [[] for i in range(0, size)]
        self.size = size
        self.option = option
        self.p = p
        self.a = random.randrange(1, p)
        self.b = random.randrange(0, p)
    
    """ Function to calculate place in array based on key """
    def _hash_function(self, key) :
        # 0 - DIVISION METHOD
        if (self.option == 0) :
            return (key % self.size)
        # 1 - MULTIPLICATION METHOD
        if (self.option == 1) :
           return (math.trunc(self.size * (key * KNUTH % 1))) 
        # 2 - UNIVERSAL HASHING
        if (self.option == 2) :
            return (((self.a * key + self.b) % self.p) % self.size)
        

    """ Print whole hash map """
    def print_map(self) :
        for list in self.array :
            if len(list) != 0 :
                for j in list :
                    print("[ Key: ", j.key, " Literal: ", j.literal, " ]")

    """ Inserting elements to hash map
        function returns -1 if there was
        item in list with same key and updates
        it's literal. If there was no item with 
        that key function returns slot in array to where
        it was appended
     """
    def insert(self, data) :
        slot = self._hash_function(data.key)
        for items in self.array[slot] :
            if (items.key == data.key) :
                # if there is already item with same key
                # just update it's literal
                item.literal = data.literal
                return -1
        self.array[slot].append(data)
        return slot

    """ Search for item in list with input key,
        if item is found then it's returned, if
        there is no item with that key value,
        None is returned
    """
    def search(self, key) :
        slot = self._hash_function(key)
        if(len(self.array[slot]) == 0) :
            return None
        else :
            #If for goes all the way it means
            #there are some items in that bucket
            #but there is no item with specified key
            #so None is returned
            for item in self.array[slot] :
                if item.key == key :
                    return item
            return None
    
    """ Tries to delete data from hash table
    """
    def delete(self, data) :
        slot = self._hash_function(data.key)
        if(len(self.array[slot]) == 0) :
            return False #No such data in hash map
        else :
            for i in range(0, len(self.array[slot])) :
                if (self.array[slot][i].key == data.key) :
                    del self.array[slot][i]
                    return True #Item deleted
            return False #Went through whole for loop and there was no specified data


#Main

hashMap = HashMap(10, 2, 23)

list = random_list(0, 20, 10)
print("Sample list \t", list)
print()

for i in list :
    data = Data(i)
    hashMap.insert(data)

hashMap.print_map()


key_to_search = 23
print("Key i'll be searching", key_to_search)
temp = hashMap.search(key_to_search)

if(temp != None) :
    print("Key found and it is : ", temp.literal)
else :
    print("No such item")


key_to_search = list[6]
print("Key i'll be searching", key_to_search)
temp = hashMap.search(key_to_search)

if(temp != None) :
    print("Key found and it is : ", temp.literal)
else :
    print("No such item")

deleted = hashMap.delete(temp)

if(deleted) :
    print("Item : ", temp.literal, " succesfully deleted ")
else :
    print(temp.literal, " no such data ")

print()

hashMap.print_map()

hashMap.insert(Data(133))

print()

hashMap.print_map()

