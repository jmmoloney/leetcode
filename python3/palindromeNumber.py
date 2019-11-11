"""palindromeNumber.py
Solution to the palindrome number problem:
        https://leetcode.com/problems/palindrome-number/"""
import argparse
from math import floor

CLI = argparse.ArgumentParser(description="palindrome number problem")
CLI.add_argument(
    "-num", type=int, default=121, help="Number to determine if palindrome or not.",
)


class Solution(object):
    def isPalindrome(self, num):
        """Determines if the given number is a palindrome or not.

        Parameters
        ----------
        num : int
            Number to determiine if palindrome or not.

        Returns
        -------
        bool
            Boolean result if the number is a palindrome or not.

        """
        return str(num) == str(num)[::-1]

    def isPalindrome_alt(self, num):
        """Determines if the given number is a palindrome or not (without
        converting to string).

        Parameters
        ----------
        num : int
            Number to determiine if palindrome or not.

        Returns
        -------
        bool
            Boolean result if the number is a palindrome or not.

        """
        if num > 0:
            num = str(num)
            half = floor(len(str(num)) / 2)
            print(num[:half])
            print(num[half + 1 :])
            return num[:half] == num[half + 1 :]


if __name__ == "__main__":
    args = CLI.parse_args()
    num = args.num

    solution = Solution()
    result = solution.isPalindrome_alt(num)
    print(result)
