from sumtripper.ad_sum import ad_sum


def test_ad_sum():
    x = ad_sum(5,5)
    assert x == 10, "Should be 10"