"""
QUESTION:
According to Gary Chapman, marriage counselor and the author of ["The Five Love Languages"](https://en.wikipedia.org/wiki/The_Five_Love_Languages) books, there are five major ways to express our love towards someone: *words of affirmation, quality time, gifts, acts of service,* and *physical touch*. These are called the love languages. Usually, everyone has a main language: the one that he/she "speaks" and understands best. In a relationship, it's import to find your partner's main love language, so that you get along better with each other.

## Your task

Unfortunately, your relationship got worse lately... After a long discussion with your partner, you agreed to give yourself a few weeks to improve it, otherwise you split up...

You will be given a `partner` instance, and `n` weeks. The `partner`  has a `.response` method, and the responses may be: `"positive"` or `"neutral"`. You can try to get a response once a day, thus you have `n * 7` tries in total to find the main love language of your partner!

```if-not:haskell
The love languages are: `"words", "acts", "gifts", "time", "touch"` (available predefined as `LOVE_LANGUAGES`)
```
```if:haskell
The love languages are: `Words, Acts, Gifts, Time, Touch` ( available `Preloaded` as `LoveLanguage` )
```

Note: your partner may (and will) sometimes give a positive response to any love language ("false positive"), but the main one has a much higher possibility. On the other hand, you may get a neutral response even for the main language, but with a low possibility ("false negative").

There will be 50 tests. Although it's difficult to fail, in case you get unlucky, just run the tests again. After all, a few weeks may not be enough...

## Examples

```python
main love language: "words"

partner.response("words") ==> "positive"
partner.response("acts")  ==> "neutral"
partner.response("words") ==> "positive"
partner.response("time")  ==> "neutral"
partner.response("acts")  ==> "positive"    # false positive
partner.response("gifts") ==> "neutral"
partner.response("words") ==> "neutral"     # false negative
etc.
```

~~~if:haskell
## Notes

`Preloaded` exports the following:

~~~

Happy coding, and **DO** try this at home! :-)

---

## My other katas

If you enjoyed this kata then please try [my other katas](https://www.codewars.com/collections/katas-created-by-anter69)! :-)

#### *Translations are welcome!*
"""

def find_main_love_language(partner, weeks):
    LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]
    responses_count = [0, 0, 0, 0, 0]
    
    for i in range(weeks * 7):
        language_index = i % 5
        if partner.response(LOVE_LANGUAGES[language_index]) == 'positive':
            responses_count[language_index] += 1
    
    main_language_index = responses_count.index(max(responses_count))
    return LOVE_LANGUAGES[main_language_index]