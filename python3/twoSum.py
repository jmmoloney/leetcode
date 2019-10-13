"""twoSum.py
Solution to the two-sum problem: https://leetcode.com/problems/two-sum/"""
import argparse

CLI = argparse.ArgumentParser(description="twoSum problem")
CLI.add_argument(
    "-nums",
    nargs="*",
    type=int,
    default=[2, 7, 11, 15],
    help="Numbers to be considered in the solution (e.g `2 7 11 15`)")

CLI.add_argument(
    "-target",
    type=int,
    default=9,
    help="Target number to search"
)

CLI.add_argument(
    "--solution",
    type=str,
    default="linear",
    choices=["linear", "n2"],
    help="Which solution to implement"
)

class Solution(object):
    def twoSum_n2(self, nums, target):
        """Searches the list and returns the indices of the two numbers that
        add to the target. Assumes exactly one solution.

        O(n^2) implementation of solution.

        Parameters
        ----------
        nums : array(int)
            Array of integers to search over.
        target : int
            Target number, the sum of two elements in nums.

        Returns
        -------
        array(int)
            Returns the indices of the two numbers that sum to target.
            None if no solution exists.

        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return[i, j]

    def twoSum(self, nums, target):
        """Searches the list and returns the indices of the two numbers that
        add to the target. Assumes exactly one solution.

        Parameters
        ----------
        nums : array(int)
            Array of integers to search over.
        target : int
            Target number, the sum of two elements in nums.

        Returns
        -------
        array(int)
            Returns the indices of the two numbers that sum to target.
            None if no solution exists.

        """
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining not in seen:
                seen[num] = i
            else:
                return [seen[remaining], i]


if __name__ == "__main__":
    args = CLI.parse_args()
    nums = args.nums
    target = args.target

    solution = Solution()
    if args.solution == "linear":
        print("linear solution:")
        result = solution.twoSum(nums, target)
    else:
        print("n2 solution:")
        result = solution.twoSum_n2(nums, target)
    print(result)
