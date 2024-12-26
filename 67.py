class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (a == '0' and b == '0'):
            return "0"
        else:
            val_a = 0
            val_b = 0
            for i in range(len(a)):
                if (a[i] == '1'):
                    val_a += 2 ** (len(a) - i - 1)
            for i in range(len(b)):
                if (b[i] == '1'):
                    val_b += 2 ** (len(b) - i - 1)
            sum_a_b = val_a + val_b
            sum_string = ""
            while sum_a_b != 0:
                sum_string = str(sum_a_b % 2) + sum_string
                sum_a_b = sum_a_b // 2
        return sum_string
