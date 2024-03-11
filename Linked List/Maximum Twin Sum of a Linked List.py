class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

    # Step 2: Iterate over the first half of the array and calculate twin sum
        max_twin_sum = float('-inf')
        n = len(values)
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_twin_sum = max(max_twin_sum, twin_sum)

        return max_twin_sum
