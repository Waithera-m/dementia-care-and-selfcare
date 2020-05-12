import unittest
from app.models import DementiaNews

class ItemTest(unittest.TestCase):

    '''
    Tests Item class behavior
    '''
    def setUp(self):

        '''
        Method runs before every test
        '''
        self.new_item = DementiaNews('Daniel Palmer', 'Coinbase Launches Price Oracle Aimed to Reduce Systemic Risk in the DeFi Space','2020-04-24T08:43:18Z','With around a billions dollars sitting in decentralized finance (DeFi) apps and protocols, Coinbase has started to provide a data feed for cryptocurrency prices to help keep those funds secure','https://www.coindesk.com/coinbase-launches-price-oracle-aimed-to-reduce-systemic-risk-in-the-defi-space','https://i.guim.co.uk/img/media/a56a52fab7991eb98c2a130cb640d20d7e460fd5/0_0_500_300/master/500.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=55f040c1c22f8a76b7b4514f8eaf1569')

    def test_instance(self):

        '''
        Function tests object initialization
        '''
        self.assertTrue(isinstance(self.new_item,DementiaNews))