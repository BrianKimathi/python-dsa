class SequenceIterator:

    def __init__(self, sequence):

        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()
        
    def __iter__(self):
        return self
    

if __name__ == '__main__':

    seq1 = SequenceIterator([2, 4, 1])

    print(seq1.__next__())
    print(seq1.__next__())
    print(seq1.__next__())