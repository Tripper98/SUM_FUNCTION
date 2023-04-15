from sumtripper.ad_sum import ad_sum, sum_list


def test_ad_sum():
    x = ad_sum(5,5)
    assert x == 10, "Should be 10"


def test_sum_list():
    x = sum_list(5,5,5)
    assert x == 15, "Should be 15"