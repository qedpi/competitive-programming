class StringHalving:
    def lexsmallest(self, s):
        """
        " Remove a copy of each char in s, so that s' is lexigraphically smallest, return first char.
        :param s: string, comprises of letters from a-z, each appearing twice
        :return: smallest
        """

        # abstraction
        # find first char of s', not s' itself

        # intuition
        # can keep discarding characters... ?
        # if we see a char twice, then we must keep one of them
        # ignore rest of the string

