# Save this in a file named test_exercises.py

### --- EXERCISE 1 ---
class Dictionary:
    def __init__(self):
        self.entries = {}
    def newentry(self, word, definition):
        self.entries[word] = definition
    def look(self, word):
        return self.entries.get(word, f"Can't find entry for {word}")

def test_dictionary():
    d = Dictionary()
    d.newentry('Apple', 'A fruit')
    assert d.look('Apple') == 'A fruit'
    assert d.look('Banana') == "Can't find entry for Banana"

### --- EXERCISE 2 ---
def get_total(costs, items, tax):
    subtotal = sum(costs[item] for item in items if item in costs)
    return round(subtotal * (1 + tax), 2)

def test_get_total():
    costs = {'socks': 5, 'shoes': 60}
    assert get_total(costs, ['socks', 'shoes'], 0.09) == 70.85

### --- EXERCISE 3 ---
def nth_char(words):
    return "".join(word[i] for i, word in enumerate(words))

def test_nth_char():
    assert nth_char(["yoda", "best", "has"]) == "yes"
    assert nth_char(["hello", "view", "mother"]) == "hit"