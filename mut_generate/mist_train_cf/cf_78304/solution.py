"""
QUESTION:
Create a MongoDB aggregation function `sortAndBin` that bins the `income` field into ranges to ensure uniqueness and then sorts the results by `binnedIncome` and `age` in ascending order. The bin size should be adjustable and the function should consider performance implications.
"""

def sortAndBin(bin_size):
    pipeline = [
      {
        "$project": {
          "binnedIncome": {
            "$floor": {
              "$divide": ["$income", bin_size]
            }
          },
          "age": 1
        },
      },
      {
        "$sort": {
          "binnedIncome": 1,
          "age": 1
        }
      }
    ]
    return pipeline