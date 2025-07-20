import random

class SequenceFile():
    def __init__(self, filename):
        self.filename=filename

    def get_sequence_dictionary(self):
        seqs: dict[int: set[str]] = dict()
        GROUP = 0

        with open(self.filename) as f:
            for line in f:
                if line[0] == 'GROUP':
                    GROUP = int(line[1])
                    seqs[GROUP] = {}
                elif line[0] == 'GRADE:':
                    pass
                else:
                    seqs[GROUP].add(line[0])

        return seqs

    def get_shuffled_list(self):
        list_seqs = []

        with open(self.filename) as f:
            for one_line in f:
                line = one_line.split()
                if line[0] == 'GROUP' or line[0] == 'GRADE:':
                    print(line)
                    pass
                else:
                    print('****', line)
                    list_seqs.append(line[0])
        random.shuffle(list_seqs)
        return list_seqs
