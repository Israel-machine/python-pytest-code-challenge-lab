from palindrome import longest_palindromic_substring

def test_longest_palindromic_substring():
    #if string is all caps
    assert longest_palindromic_substring("RACECAR BOB ") == "racecar"
    #if string is all lowercase
    assert longest_palindromic_substring("racecar bob") == "racecar"
    #if string is mixed numbers
    assert longest_palindromic_substring("1o11") == "1o1"
    #if string is mixed caps
    assert longest_palindromic_substring("Bobby") == "bob"
    #if string is one word
    assert longest_palindromic_substring("Timmy") == "mm"
    #if string is multiple words
    assert longest_palindromic_substring("Racecar Bob") == "racecar"
    #if string is one character
    assert longest_palindromic_substring("i") == "i"
    #if string empty
    assert longest_palindromic_substring("") == ""
    #if string is only numbers
    assert longest_palindromic_substring("567888") == "888"
    #if string includes special characters
    assert longest_palindromic_substring("@@@llen 3eeB Bobbob") == "bobbob"