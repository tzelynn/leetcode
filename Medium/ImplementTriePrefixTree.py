# link: https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Trie:

    def __init__(self):
        self.storage = {}

    def insert(self, word: str) -> None:
        curr = self.storage
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["end"] = True

    def search(self, word: str) -> bool:
        curr = self.storage
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return "end" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.storage
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)