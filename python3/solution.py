"""solution.py
Template solution for leetcode problems.
Solution to the {} problem: https://leetcode.com/problems/reverse-integer/"""
import argparse

CLI = argparse.ArgumentParser(description="{} problem")
CLI.add_argument(
    "-num",
    type=int,
    default=100,
    help="Number")

class Solution(object):
    def number(self, num):
        """Short summary.

        Parameters
        ----------
        num : type
            Description of parameter `num`.

        Returns
        -------
        type
            Description of returned object.

        """
        return num

if __name__ == "__main__":
    args = CLI.parse_args()
    num = args.num

    solution = Solution()
    result = solution.number(num)
    print(result)
