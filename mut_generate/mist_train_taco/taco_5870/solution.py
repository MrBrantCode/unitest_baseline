"""
QUESTION:
Chef Loves to listen to remix songs, but currently he had already finished the entire playlist of remix songs.
As Chef is smart, so he thought let's make my own remix songs of the original songs.
Chef is not having much knowledge of making remix songs, so he came up with the simple technique in which he will pick the word which contains the smallest number of characters from the lyrics of the song, and then he will append that word to the start and end of the lyrics, also Chef will insert this word between every two words of the lyrics.
Note: While inserting a new word Chef will also insert extra white-spaces, so that every word in the final remixed lyrics is separated by space.
It is Recommended to use fast Input/Ouput techniques.

-----Input:-----
- The input contains the text $S$, which denotes the lyrics of the song.

-----Output:-----
- Print the Remixed, lyrics as done by Chef.

-----Constraints:-----
- $1 \leq Length of text $S$ \leq 10^7$

-----Sample Input:-----
Mai Hu Jiyaan

-----Sample Output:-----
Hu Mai Hu Hu Hu Jiyaan Hu
"""

def remix_lyrics(S: str) -> str:
    # Split the input lyrics into words
    words = S.split()
    
    # Find the word with the smallest number of characters
    min_length = float('inf')
    smallest_word = ''
    for word in words:
        if len(word) < min_length:
            min_length = len(word)
            smallest_word = word
    
    # Construct the remixed lyrics
    remixed_lyrics = smallest_word
    for word in words:
        remixed_lyrics += ' ' + word + ' ' + smallest_word
    
    return remixed_lyrics