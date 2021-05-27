import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price) / 2
      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price) / 2
      self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price))

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_BidNotNegative(self):
    quotes = [
      {'top_ask': {'price': 132.25, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 131.63, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 140.56, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 139.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """Assertion"""
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertGreater(bid_price, 0)

  def test_getDataPoint_AskNotNegative(self):
    quotes = [
      {'top_ask': {'price': 55.34, 'size': 86}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 54.95, 'size': 153}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 67.92, 'size': 14}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 66.12, 'size': 98}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertGreater(ask_price, 0)

  def test_getDataPoint_calculatePriceNotNegative(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertGreater((price, 0))
      
  """getRatio tests"""
  def test_getRatio_calculateRatioGreaterThanOne(self):
    price_a = 279.44
    price_b = 182.04

    self.assertGreater(getRatio(price_a, price_b), 1)

  def test_getRatio_calculateRatioLessThanOne(self):
    price_a = 92.99
    price_b = 126.63

    self.assertLess(getRatio(price_a, price_b), 1)

  def test_getRatio_calculateRatioExactlyOne(self):
    price_a = 442.34
    price_b = 442.34

    self.assertEqual(getRatio(price_a, price_b), 1)

  def test_getRatio_divideByZeroReturnNone(self):
    price_a = 89.74
    price_b = 0

    self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_zeroDividedByPriceReturnZero(self):
    price_a = 0
    price_b = 253.63  

    self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_ratioNotNegative(self):
    price_a = 123.43
    price_b = 111.83

    self.assertGreater(getRatio(price_a, price_b), 0)


if __name__ == '__main__':
    unittest.main()
