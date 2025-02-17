class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        min_open, max_open = 0, 0

        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0': # If the locked value is 0 then it isn't important whether it is open or not.
                max_open += 1
            
            else:
                max_open -= 1 # the reason why the max_open is decremented is becasue if the locked value is 1 and it is a ')' then we know that this must cancel out the '(' there is

            if s[i] == ')' and locked[i] == '1': # if not ( then it must be ), this means that we must at bare minimum have min_open breackets if this is zero then we are fine, if min_open < 0, then there must be unmatched brackets
                min_open += 1

            else:
                min_open -= 1 # decrements the count as it must be a locked ( bracket.


            if max_open < 0:
                return False

            min_open = max(min_open, 0) 

            if min_open > 0:
                return False

            return True
