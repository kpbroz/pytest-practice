from hello import prime_minister, chief_minister


def test_prime_minister():
    assert "Narendra Modi" == prime_minister()


def test_chief_minister():
    assert "Siddaramayya" == chief_minister()
