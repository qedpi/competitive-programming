class StringHalving:
    def lexsmallest(self, s):
        """
        :param s: string, comprising chars from a-z, each appearing twice
        :return: return first char of s', substring of s:
        "           lexigraphically smallest
        "           contains one copy of each char
        """
        # Abstraction: don't need s'


        # Intuition


        # Pseudocode
        # keep a set of chars seen
        seen = set()
        # go through string, adding chars to set
        for c in s:
        # if char already seen
            if c in seen:
        # return min of that set
                return min(seen)
            seen.add(c)
            
        # Test cases
        # bacabc
        # Plan A: can discarding chars as long as cur  > next

        # dbcaabcd
        # Plan B: min(it) min(s) => min char

        # [cbc]
        # min(s) = a




















        # abstraction
        # find first char of s', not s' itself

        # intuition
        # can keep discarding characters... ?
        # if we see a char twice, then we must keep one of them
        # ignore rest of the string

