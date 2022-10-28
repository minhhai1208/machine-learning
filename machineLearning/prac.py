import sys


class Node:


    def __init__(self, value):
        self.value = value
        self.children = dict()
        self.end = False  # indicates if this is an exit node

    def __getitem__(self, key):
        if key in self.children:
            return self.children[key]
        return None

    def __setitem__(self, key, value):
        self.children[key] = value

    def __contains__(self, value):
        return value in self.children

    def __str__(self):
        return str(self.value)


class Trie:
    def __init__(self):
        self.root = Node('')

    def add(self, word):

        word = word.strip()
        n = self.root  # n is for "node"
        for l in word:
            nxt = n[l]  # nxt is for the next node in the trie
            if nxt is not None:
                n = nxt
            else:
                n[l] = Node(l)
                n = n[l]
        n.end = True

    def __contains__(self, word):

        n = self.root  # n is for "node"
        for l in word:
            if l not in n:
                return False
            n = n[l]
        if n.end == True:
            return True
        return False


class SpellCheck:

    def __init__(self):

        self.words = Trie()
        with open('/usr/share/dict/words', 'r') as f:
            for word in f:
                self.words.add(word)

    def spellcheck(self, word):


        # Try the word
        if word in self.words:
            return word

        # Try lowercase
        word = word.lower()
        if word in self.words:
            return word

        vowels = 'aeiou'  # let's not consider 'y' a vowel in this case

        def recurse(path, word, node):


            # base cases
            if node is None:
                return None
            if word == '':
                if node.end == True:
                    return path
                if node.end == False:
                    return None

            # try the letter
            ltr = word[0]
            if ltr in node:
                result = recurse(path + ltr, word[1:], node[ltr])
                if result:
                    return result

            # try lowercase
            ltr = ltr.lower()
            if ltr in node:
                result = recurse(path + ltr, word[1:], node[ltr])
                if result:
                    return result

            # try skipping duplicates
            if len(word) > 1 and ltr == word[1]:
                result = recurse(path, word[1:], node)
                if result:
                    return result

            # try replacing vowels
            if ltr in vowels:
                for v in vowels:
                    if v != ltr:
                        result = recurse(path + v, word[1:], node[v])
                        if result:
                            return result

            return None

        result = recurse('', word, self.words.root)
        if result:
            return result
        return 'NO SUGGESTION'


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        t = Trie()
        # Test trie
        with open('/usr/share/dict/words', 'r') as f:
            for word in f:
                word = word.strip()
                t.add(word)
                try:
                    assert (word in t)
                except AssertionError:
                    print
                    word, "not in trie"
                    sys.exit(1)

        # Run doctests
        s = SpellCheck()
        import doctest

        doctest.testmod(extraglobs={'s': s})
        sys.exit(0)

    s = SpellCheck()
    while True:
        word = "aple"
        print(s.spellcheck(word))