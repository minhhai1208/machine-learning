class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:

            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:

            print(word)

        for a, n in node.children.items():

            self.suggestionsRec(n, word + a)


    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root
        i = 0
        if not node.children.get(key[0]):
            return 1
        for a in key:
            # no string in the Trie has this prefix

            if not node.children.get(a):
                key = key[0:i]
                self.suggestionsRec(node,key)
                return 0


            node = node.children[a]
            i +=1

        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not node.children:
            return -1

        self.suggestionsRec(node,key)



        return 1


    def check_spell(self,node,word):
        if node.children.values() == " ":
            return word

        for a, n in node.children.items():

            self.check_spell(n, word + a)


# Driver Code
keys = ["Nguyễn Văn Cừ, phuong 5, quan 1", "Trần Hưng Đạo, p4, q1", "Nguyễn Thị Thập, p5, quận 7"
      , "Đại Học Kinh Tế", "Đại Học Bách Khoa", "Đại Học FPT, Lô E2a-7, Đường D1, Đ. D1, Long Thạnh Mỹ, Thành Phố Thủ Đức, Thành phố Hồ Chí Minh 700000"]  # keys to form the trie structure.


t = Trie()

# creating the trie structure with the
# given set of strings.

t.formTrie(keys)


key = "b"
while key != "a":
    key = input("Enter: ")
    comp = t.printAutoSuggestions(key)


# creating trie object

# autocompleting the given key using
# our trie structure.





# This code is contributed by amurdia and muhammedrijnas