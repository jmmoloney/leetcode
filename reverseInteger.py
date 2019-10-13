"""reverseInteger.py
Solution to the reverse integer problem: https://leetcode.com/problems/reverse-integer/"""
import argparse

CLI = argparse.ArgumentParser(description="reverseInteger problem")
CLI.add_argument(
    "-num",
    type=int,
    default=-123,
    help="Number to reverse (can be negative) (e.g `-123`)")

class Solution(object):
    def reverse(self, x):
        """Given a 32-bit signed integer x, reverse digits of an integer.

        Parameters
        ----------
        x : int
            Number to reverse.

        Returns
        -------
        int
            Reverse number.
            If overflows from 32-bit signed integer, returns 0.

        """
        if x < 0:
            x = x*(-1)
            x = str(x)[::-1]
            x = -1*int(x)
        else:
            x = int(str(x)[::-1])
        # check for overflow
        if x < -2**31 or x > (2**31)-1:
            x = 0
        return x

if __name__ == "__main__":
    args = CLI.parse_args()
    x = args.x

    solution = Solution()
    result = solution.reverseInteger(x)
    print(result)
