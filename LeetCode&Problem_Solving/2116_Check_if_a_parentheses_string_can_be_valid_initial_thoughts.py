

class Solution(object):
    """
        :type s: str
        :type locked: str
        :rtype: bool
    """

    '''
        Requirements:
        - The number of open brackets and close brackets must be the same.
        - It is not necessary to have even number of brackets.
        
        Method:
        1. Create two 2d arrays one for the locked and the other for the unlocked brackets.
        2. The 0th index of the 2d array will contain the bracket itself, then the next index will store which bracket it was from the string s.
        3. The number of open brackets must be able to be equal to the number of closing brackets

    '''

    def changeableBrackets(self, s, locked):
        changeable = [[]]
        for bracket in range(0, len(s)):
            if locked[bracket] == '0':
                changeable.append([s[bracket], bracket])

        return changeable

    def unchangeableBrackets(self, s, locked):
        unchangeable = [[]]
        for bracket in range(0, len(s)):
            if locked[bracket] == '1':
                unchangeable.append([s[bracket], bracket])

        return unchangeable
   
   
    def canBeValid(self, s, locked):
        validated = False

        changeable = self.changeableBrackets(s, locked)
        unchangeable = self.unchangeableBrackets(s, locked)

        closing_count = 0
        openning_count = 0

        # First check if the lenght of the array s is even
        if len(s) % 2 != 0:
            return False
        
        for bracket in unchangeable:
            if bracket == ")":
                closing_count += 1
            
            else:
                openning_count += 1

        for bracket in changeable:
            if closing_count < openning_count:
                closing_count += 1

            else:
                openning_count += 1

        if closing_count == openning_count:
            return True

        return False           

