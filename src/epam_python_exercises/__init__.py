def main() -> None:
    print("Hello from epam-python-exercises!")


### --- EXERCISE 1: Dictionary Class ---
class Dictionary:
    def __init__(self):
        # Initialize an empty dictionary to store our data
        self.entries = {}

    def newentry(self, word, definition):
        # Add the word as a key and definition as the value
        self.entries[word] = definition

    def look(self, word):
        # Return the definition if it exists, otherwise return the error message
        return self.entries.get(word, f"Can't find entry for {word}")


# Testing Exercise 1
print("--- Exercise 1: Dictionary ---")
d = Dictionary()
d.newentry("Apple", "A fruit that grows on trees")
print(f"Lookup 'Apple': {d.look('Apple')}")  # Expected: A fruit that grows on trees
print(f"Lookup 'Banana': {d.look('Banana')}")  # Expected: Can't find entry for Banana
print("-" * 30)


### --- EXERCISE 2: Total Spend Calculator ---
def get_total(costs, items, tax):
    # Sum up the cost for each item if it exists in the dictionary
    # If the item doesn't exist, it is ignored
    subtotal = sum(costs[item] for item in items if item in costs)

    # Calculate the total including tax
    total = subtotal * (1 + tax)

    # Return the total rounded to two decimal places
    return round(total, 2)


# Testing Exercise 2
print("--- Exercise 2: Total Spend ---")
costs_dict = {"socks": 5, "shoes": 60, "sweater": 30}
items_bought = ["socks", "shoes"]
tax_rate = 0.09

result = get_total(costs_dict, items_bought, tax_rate)
print(f"Total spent: {result}")  # Expected Output: 70.85
print("-" * 30)


### --- EXERCISE 3: N-th Letter Word Construction ---
def nth_char(words):
    result = "asdfs"
    # Use enumerate to get the index (n) and the word
    for n, word in enumerate(words):
        # Add the character at index n to our result string
        result += word[n]
    return result


# Testing Exercise 3
   print("--- Exercise 3: N-th Character ---")
word_list1 = ["yoda", "best", "has"]
word_list2 = ["hello", "view", "mother"]

print(f"Result 1: {nth_char(word_list1)}")  # Expected: "yes" (y[0], e[1], s[2])
print(f"Result 2: {nth_char(word_list2)}")  # Expected: "hit" (h[0], i[1], t[2])
# print(f"Result 1 (Manual Check): {nth_char(word_list1)}") # Correctly uses word_list1
