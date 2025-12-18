"""
QUESTION:
You wrote all your unit test names in camelCase.
But some of your colleagues have troubles reading these long test names.
So you make a compromise to switch to underscore separation.

To make these changes fast you wrote a class to translate a camelCase name
into an underscore separated name.

Implement the ToUnderscore() method.

Example:

`"ThisIsAUnitTest" => "This_Is_A_Unit_Test"`


**But of course there are always special cases...**

You also have some calculation tests. Make sure the results don't get split by underscores.
So only add an underscore in front of the first number.

Also Some people already used underscore names in their tests. You don't want to change them.
But if they are not split correct you should adjust them.

Some of your colleagues mark their tests with a leading and trailing underscore.
Don't remove this.

And of course you should handle empty strings to avoid unnecessary errors. Just return an empty string then.

Example:

`"Calculate15Plus5Equals20" => "Calculate_15_Plus_5_Equals_20"`

`"This_Is_Already_Split_Correct" => "This_Is_Already_Split_Correct"`

`"ThisIs_Not_SplitCorrect" => "This_Is_Not_Split_Correct"`

`"_UnderscoreMarked_Test_Name_" => _Underscore_Marked_Test_Name_"`
"""

import re

def convert_camel_to_underscore(name: str) -> str:
    if not name:
        return ""
    
    # Handle leading and trailing underscores
    leading_underscore = name.startswith('_')
    trailing_underscore = name.endswith('_')
    
    # Remove leading and trailing underscores for processing
    if leading_underscore:
        name = name[1:]
    if trailing_underscore:
        name = name[:-1]
    
    # Convert camelCase to underscore_separated
    name = re.sub('(?<=[^_-])_?(?=[A-Z])|(?<=[^\\d_])_?(?=\\d)', '_', name)
    
    # Re-add leading and trailing underscores if they were present
    if leading_underscore:
        name = '_' + name
    if trailing_underscore:
        name += '_'
    
    return name