#!python


from __future__ import division, print_function


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            # TODO: increment item count
            # Checking if the item exist in the object (Dictionary)
            if item not in self:
                # if not initialize the key's value as 1
                self[item] = 1
            else:
                # if it already exist increment the value by 1
                self[item] += 1
        # The number of distinct item in the dictionary, just list down all the dictionary keys.
        self.types = len(self.keys())
        # The number of tokens, sum function to add all values in the dictionary
        self.tokens = sum(self.values())
        pass

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if self.get(item) < 1:
            return 0
        return self.get(item)


class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            # Checking if the item exist or not using __contains__ function
            if self.__contains__(item):
                # if yes change the data type of the element into list
                # this is because tuple is immutable
                self[self._index(item)] = list(self[self._index(item)])
                # increment the frequency of the word
                self[self._index(item)][1] += 1
                # change again the datatype of the element into the original
                self[self._index(item)] = tuple(self[self._index(item)])
            else:
                # if the item not exist, initialize the frequency with 1
                # append a tuple into the list
                self.append((item, 1))
        # distinct value is the length of the self array
        self.types = len(self)
        # using list_comprehension in order to list down all the frequency
        # sum function helps to add every frequency in the list_comprehension
        # assign the value of the sign into Tokens.
        self.tokens = sum([x[1] for x in self])
        pass

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        for index_tuple, item_tuple in enumerate(self):
            if self[index_tuple][0] == item:
                return self[index_tuple][1]
        return 0
        pass

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        for index_tuple, item_tuple in enumerate(self):
            if self[index_tuple][0] == item:
                return True
        return False
        pass

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        for index_tuple, item_tuple in enumerate(self):
            if self[index_tuple][0] == target:
                return index_tuple
                pass


def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)

    hist_list = Listogram(text_list)
    print('listogram:', hist_list)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
