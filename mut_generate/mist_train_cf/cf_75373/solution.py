"""
QUESTION:
Write a function `largestOverlap` that takes two square binary matrices `img1` and `img2` of size `n x n` as input, where `n` ranges from 1 to 30, and returns the maximum possible overlap of 1s when `img1` is translated in any direction (left, right, up, or down) by any number of units and superimposed on `img2`. The overlap is defined as the count of positions where both images have a 1. Note that rotation is not allowed.
"""

def largestOverlap(img1, img2):
    def shift_and_count(x_shift, y_shift, M, R):
        count = 0
        for r_row, m_row in enumerate(range(y_shift, len(M))):
            for r_col, m_col in enumerate(range(x_shift, len(M))):
                if M[m_row][m_col] == R[r_row][r_col] == 1:
                    count += 1
        return count

    def create_convolution(M, R):
        size = len(M)
        max_overlaps = 0
        # translation on x-axis
        for x_shift in range(size):
            # translation on y-axis
            for y_shift in range(size):
                max_overlaps = max(max_overlaps,
                                   shift_and_count(x_shift, y_shift, M, R))
        return max_overlaps

    return max(create_convolution(img1, img2), create_convolution(img2, img1))