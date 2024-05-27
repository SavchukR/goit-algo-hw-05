class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def delete(self, key):
        key_hash = self.hash_function(key)
        
        if self.table[key_hash] is None:
            return None
        
        hash_node = self.table[key_hash]
        
        for pair in hash_node:
            if pair[0] == key:
                hash_node.remove(pair)
                return True
            
    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
 
    def print_table(self):
        elements = []
        for bucket in self.table:
            subelements = []
            for pair in bucket:
                subelements.append(f"[{pair[0]}: {pair[1]}]")
            elements.append('[' + ' | '.join(subelements) + "]")
        return '[' + ', '.join(elements) + "]"

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.insert("ananas", 40)
H.insert("ananaso", 50)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30
print(H.get("ananas"))  
print(H.get("ananaso"))  

print("before delete")
print(H.print_table())

H.delete('ananas')

print("after delete")
print(H.print_table())

print('Press any key to close...')
input()