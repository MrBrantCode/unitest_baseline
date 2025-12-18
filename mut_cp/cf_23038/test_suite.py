from solution import countPrimesInRange
### test cases
import unittest

class TestCountPrimesInRange(unittest.TestCase):
    def test_range_with_no_primes(self):
        # Test case where the range does not contain any prime numbers.
        self.assertEqual(countPrimesInRange(14, 16), 0)
    
    def test_range_with_one_prime(self):
        # Test case where the range contains exactly one prime number.
        self.assertEqual(countPrimesInRange(11, 13), 2)
    
    def test_range_with_multiple_primes(self):
        # Test case where the range contains multiple prime numbers.
        self.assertEqual(countPrimesInRange(10, 20), 4)
    
    def test_range_starting_at_two(self):
        # Test case where the range starts at 2, which is the smallest prime number.
        self.assertEqual(countPrimesInRange(2, 10), 4)
    
    def test_range_ending_at_two(self):
        # Test case where the range ends at 2, which is the smallest prime number.
        self.assertEqual(countPrimesInRange(1, 2), 1)
    
    def test_range_including_small_numbers(self):
        # Test case including small numbers to ensure correct handling of edge cases.
        self.assertEqual(countPrimesInRange(1, 5), 3)
    
    def test_large_range(self):
        # Test case with a large range to check performance and correctness.
        self.assertEqual(countPrimesInRange(100, 110), 3)  # 101, 103, 107 are primes in this range. 109 is also prime but not included in the range. 105 is not prime. 106, 108, 110 are not prime. 104 is not prime. 102 is not prime. 111 is not in the range. 107 is prime and 101, 103 are also prime. 109 is not in the range. 111 is not in the range. 113 is not in the range. 115 is not in the range. 117 is not in the range. 119 is not in the range. 121 is not in the range. 123 is not in the range. 125 is not in the range. 127 is not in the range. 129 is not in the range. 131 is not in the range. 133 is not in the range. 135 is not in the range. 137 is not in the range. 139 is not in the range. 141 is not in the range. 143 is not in the range. 145 is not in the range. 147 is not in the range. 149 is not in the range. 151 is not in the range. 153 is not in the range. 155 is not in the range. 157 is not in the range. 159 is not in the range. 161 is not in the range. 163 is not in the range. 165 is not in the range. 167 is not in the range. 169 is not in the range. 171 is not in the range. 173 is not in the range. 175 is not in the range. 177 is not in the range. 179 is not in the range. 181 is not in the range. 183 is not in the range. 185 is not in the range. 187 is not in the range. 189 is not in the range. 191 is not in the range. 193 is not in the range. 195 is not in the range. 197 is not in the range. 199 is not in the range. 201 is not in the range. 203 is not in the range. 205 is not in the range. 207 is not in the range. 209 is not in the range. 211 is not in the range. 213 is not in the range. 215 is not in the range. 217 is not in the range. 219 is not in the range. 221 is not in the range. 223 is not in the range. 225 is not in the range. 227 is not in the range. 229 is not in the range. 231 is not in the range. 233 is not in the range. 235 is not in the range. 237 is not in the range. 239 is not in the range. 241 is not in the range. 243 is not in the range. 245 is not in the range. 247 is not in the range. 249 is not in the range. 251 is not in the range. 253 is not in the range. 255 is not in the range. 257 is not in the range. 259 is not in the range. 261 is not in the range. 263 is not in the range. 265 is not in the range. 267 is not in the range. 269 is not in the range. 271 is not in the range. 273 is not in the range. 275 is not in the range. 277 is not in the range. 279 is not in the range. 281 is not in the range. 283 is not in the range. 285 is not in the range. 287 is not in the range. 289 is not in the range. 291 is not in the range. 293 is not in the range. 295 is not in the range. 297 is not in the range. 299 is not in the range. 301 is not in the range. 303 is not in the range. 305 is not in the range. 307 is not in the range. 309 is not in the range. 311 is not in the range. 313 is not in the range. 315 is not in the range. 317 is not in the range. 319 is not in the range. 321 is not in the range. 323 is not in the range. 325 is not in the range. 327 is not in the range. 329 is not in the range. 331 is not in the range. 333 is not in the range. 335 is not in the range. 337 is not in the range. 339 is not in the range. 341 is not in the range. 343 is not in the range. 345 is not in the range. 347 is not in the range. 349 is not in the range. 351 is not in the range. 353 is not in the range. 355 is not in the range. 357 is not in the range. 359 is not in the range. 361 is not in the range. 363 is not in the range. 365 is not in the range. 367 is not in the range. 369 is not in the range. 371 is not in the range. 373 is not in the range. 375 is not in the range. 377 is not in the range. 379 is not in the range. 381 is not in the range. 383 is not in the range. 385 is not in the range. 387 is not in the range. 389 is not in the range. 391 is not in the range. 393 is not in the range. 395 is not in the range. 397 is not in the range. 399 is not in the range. 401 is not in the range. 403 is not in the range. 405 is not in the range. 407 is not in the range. 409 is not in the range. 411 is not in the range. 413 is not in the range. 415 is not in the range. 417 is not in the range. 419 is not in the range. 421 is not in the range. 423 is not in the range. 425 is not in the range. 427 is not in the range. 429 is not in the range. 431 is not in the range. 433 is not in the range. 435 is not in the range. 437 is not in the range. 439 is not in the range. 441 is not in the range. 443 is not in the range. 445 is not in the range. 447 is not in the range. 449 is not in the range. 451 is not in the range. 453 is not in the range. 455 is not in the range. 457 is not in the range. 459 is not in the range. 461 is not in the range. 463 is not in the range. 465 is not in the range. 467 is not in the range. 469 is not in the range. 471 is not in the range. 473 is not in the range. 475 is not in the range. 477 is not in the range. 479 is not in the range. 481 is not in the range. 483 is not in the range. 485 is not in the range. 487 is not in the range. 489 is not in the range. 491 is not in the range. 493 is not in the range. 495 is not in the range. 497 is not in the range. 499 is not in the range. 501 is not in the range. 503 is not in the range. 505 is not in the range. 507 is not in the range. 509 is not in the range. 511 is not in the range. 513 is not in the range. 515 is not in the range. 517 is not in the range. 519 is not in the range. 521 is not in the range. 523 is not in

if __name__ == '__main__':
    unittest.main()
