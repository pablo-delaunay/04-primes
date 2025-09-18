from main import isprime

def test_isprime_basic():
    assert isprime(2) == True
    assert isprime(3) == True
    assert isprime(4) == False
    assert isprime(17) == True
    assert isprime(1) == False
    assert isprime(0) == False
    assert isprime(-7) == False

def test_isprime_large():
    assert isprime(97) == True
    assert isprime(99) == False
