#include <math.h>

int smallestNumber(int n) {
    for (int i = 1; i < 11; ++i) {
        if (n <= (pow(2, i) - 1)) {
            return (pow(2, i) - 1);
        }
    }

    return 0;
}
