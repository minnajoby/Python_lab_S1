def add(*args):
        """
        This function accepts a variable number of integer arguments and returns their sum.
        Parameters : *args(int) : variable length integer arguments to be added.
        """
        return sum(args)

print(f"Sum of 1, 2, 3 : {add(1,2,3)}")
