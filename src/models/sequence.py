
class SequenceBlock():
    """This class defines the sequence blocks."""
    sequence: str
    length: int
    group: int

    def __init__(self, sequence: str, length: int, group: int):
        """
        Initializes a Sequence block

        :param sequence: DNA sequence that defines the block
        :type sequence: str
        :param length: Length of sequence, and hence of the block
        :type length: int
        :param group: Group that the sequence belongs to (1-4)
        :type length: int
        """

        self.sequence = sequence
        self.length = length
        self.group = group

    def getSequence(self) -> str:
        return self.sequence

    def getLength(self) -> int:
        return self.length

    def getGroup(self) -> int:
        return self.group