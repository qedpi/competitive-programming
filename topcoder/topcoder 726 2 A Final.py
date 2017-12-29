class StringHalving:
    def lexsmallest(self, s):
        """
        :param s: string, comprising chars from a-z, each appearing twice
        :return: return first char of s', substring of s:
        "           lexigraphically smallest
        "           contains one copy of each char
        """

        seen = set()
        for c in s:
            if c in seen:
                return min(seen)
            seen.add(c)
