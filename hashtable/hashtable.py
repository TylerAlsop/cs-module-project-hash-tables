class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.number_of_items = 0
        self.head = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # self.capacity = len(HashTable)
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.number_of_items/self.capacity
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        ########### Psuedo Code ###########
        # offest_basis for 64 bit is:  14695981039346656037
        # hash = offest_basis

        # FNV_prime for 64 bit is:  2^40 + 2^8 + 0xb3 (1099511628211)

        # encode (convert) each charactrer into UTF-8 numbers.

        # for each octet of data to be hashed:
        #     hash = hash * FNV_prime
        #     hash = hash xor octet of data
        # return hash

        # "xor" in python is ^


        ########### Actual Code ###########
        FNV_prime = 2**40 + 2**8 + 0xb3
        offest_basis = 14695981039346656037
        key_encoded = key.encode()

        hash = offest_basis

        for character in key_encoded:
            hash = hash * FNV_prime
            hash = hash ^ character
        return hash



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        ########### Psuedo Code ###########


        ########### Actual Code ###########
        hash = 5381
        for character in key:
            hash = (( hash << 5) + hash) + ord(character)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        ######## Without Collision Handling ########
        # index = self.hash_index(key)
        # self.hash_table[index] = value

        ######## With Collision Handling ########
        current_load_factor = self.get_load_factor()

        if current_load_factor >= 0.7:
            self.resize(2)
        
        if current_load_factor <= 0.2:
            self.resize(0.5)

        new_entry = HashTableEntry(key, value)

        hash_table = self.hash_table
        index = self.hash_index(key)

        current_node = hash_table[index]

        if current_node is None:
            current_node = new_entry
            self.number_of_items += 1
            return
        
        while current_node is not None and current_node.key != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            previous_node.next = new_entry
            self.number_of_items += 1
        else:
            print(f"The key, '{key},' has been found and will be updated with the new value you have chosen. New Value: '{value}'")
            current_node.value == value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        ######## Without Collision Handling ########
        # if (self.hash_table[self.hash_index(key)] == None):
        #     print("Error: The key you are looking for does not exist.")
        #     return
        # else:
        #     self.hash_table[self.hash_index(key)] = None

        ######## With Collision Handling ########
        index = self.hash_index(key)
        hash_table = self.hash_table

        current_node = hash_table[index]

        if current_node.key == key:
            hash_table[index] = current_node.next
            self.number_of_items -= 1
            return
        
        while current_node is not None and current_node.key != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("Error: The key you are looking for does not exist.")
            return current_node

        previous_node.next = current_node.next
        self.number_of_items -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        ######## Without Collision Handling ########
        # if (self.hash_table[self.hash_index(key)] == None):
        #     return None
        # else:
        #     return self.hash_table[self.hash_index(key)]

        ######## With Collision Handling ########
        index = self.hash_index(key)
        hash_table = self.hash_table

        current_node = hash_table[index]

        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next
                
        if (current_node == None):
            return None
        return current_node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
####################### Resize So Number of Slots Is Multiplied By Input #######################
        # resized_hash_table = [None] * (self.capacity * int(new_capacity))

        # for i in range(len(self.hash_table)):
        #     current_node = self.hash_table[i]

        #     while current_node is not None:
        #         index = self.hash_index(current_node.key)
        #         resized_hash_table[index] = current_node
        #         current_node = current_node.next
        # self.hash_table = resized_hash_table

####################### Resize So Number of Slots Equals Input #######################

        resized_hash_table = [None] * int(new_capacity)

        for i in range(len(self.hash_table)):
            current_node = self.hash_table[i]

            while current_node is not None:
                index = self.hash_index(current_node.key)
                resized_hash_table[index] = current_node
                current_node = current_node.next
        self.hash_table = resized_hash_table
        


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
