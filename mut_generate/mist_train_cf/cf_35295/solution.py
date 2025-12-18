"""
QUESTION:
Create a function `check_redistribution_conditions` that takes a text as input and returns whether the text complies with the redistribution conditions. The function should check for the presence of four specific redistribution conditions in the input text. If all conditions are found, the function should return "Complies with redistribution conditions". Otherwise, it should return "Does not comply with redistribution conditions".
"""

def check_redistribution_conditions(text):
    conditions = [
        "Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.",
        "Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.",
        "Neither the name of Estrate nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.",
        "THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR"
    ]

    for condition in conditions:
        if condition not in text:
            return "Does not comply with redistribution conditions"
    return "Complies with redistribution conditions"