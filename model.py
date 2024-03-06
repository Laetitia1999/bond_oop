class Bond:
    def __init__(self, isin, face_value, rate, currency):
        self.isin = isin
        self.face_value = face_value
        self.rate = rate
        self.currency = currency

    def __str__(self):
        return "Bond({id}, {fv}, {r}, {curr}, {c})".format(
            id=self.isin,
            fv=self.face_value,
            r=self.rate,
            curr=self.currency,
            c=str(self.coupon()),
        )

    def coupon(self):
        return self.face_value * self.rate


def test_coupon():
    bond = Bond("FR01", 10000, 0.01, "EUR")
    expected = 100
    actual = bond.coupon()

    assert expected == actual


def test_str():
    bond = Bond("FR01", 10000, 0.01, "EUR")
    expected = "Bond(FR01, 10000, 0.01, EUR, 100.0)"
    actual = bond.__str__()
    assert expected == actual
