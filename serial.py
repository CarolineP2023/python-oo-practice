"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """initalizes generator starting at the number one"""
        self.start = self.next = start

    def __repr__(self):
        """shows representation"""
        return f"<SerialGenerator start = {self.start} next = {self.next}"
    
    def generate(self)
        """ generates the next sequential number"""
        
        self.next += 1
        return self.next -1

    def reset(self):
        """resets the number back to the original start number"""

        self.next = self.start

    

