import sys
import random
import math

def random_list(min, max, no_el) :
    list = random.sample(range(min, max), no_el)
    return list

class Data :
    def __init__(self, key) :
        self.key = key
        self.literal = str(key)

class HashTable :
    def __init__(self, size, c1 = 0.5, c2 = 0.5) :
        self.size = size
        self.array = [None for i in range(0, size)]
        self.c1 = c1
        self.c2 = c2

    def hash1(self, key) :
        return (key % self.size)

    def hash(self, key, i) :
        return int((self.hash1(key) + self.c1 * i + self.c2 *i * i) % self.size)

    def print(self) :
        for item in self.array :
            if(item != None) :
                print("[ Key: ", item.key, " Literal: ", item.literal, " ]")
        print()

    def insert(self, data) :
        print("Inserting data with key ", data.key, "...")
        i = 0
        while(1) :
            slot = self.hash(data.key, i)
            if(self.array[slot] == None) :
                self.array[slot] = data
                print("Insert successfull")
                return True
            else :
                if(self.array[slot].key == data.key) :
                    self.array[slot].literal = data.literal
                    print("Data updated succesfully")
                    return True
            i += 1
            if(i == self.size) :
                break
        print("Failed inserting item to table, table is full !")
        return False

    def search(self, key) :
        print("Searching for ", key, "...")
        i = 0
        while(1) :
            slot = self.hash(key, i)
            if(self.array[slot] == None) :
                print("No such item in list")
                return None
            else :
                if(self.array[slot].key == key) :
                    print("Found item with key", key, "and literal is", self.array[slot].literal)
                    return self.array[slot]

                i += 1
                if(i == self.size) :
                    break

        print("No such item in list")
        return False


#Main

hash_table = HashTable(6)

hash_table.insert(Data(1))
hash_table.print()

hash_table.insert(Data(2))
hash_table.print()

hash_table.insert(Data(3))
hash_table.print()

hash_table.insert(Data(505))
hash_table.print()

hash_table.insert(Data(10004))
hash_table.print()

hash_table.insert(Data(0))
hash_table.print()

hash_table.insert(Data(505))

hash_table.search(505)
hash_table.search(12345)
hash_table.search(2)

hash_table.insert(Data(12345))
hash_table.insert(Data(0))

hash_table.insert(Data(505))
