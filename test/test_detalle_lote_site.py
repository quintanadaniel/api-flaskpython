import unittest
from modules.detail_lote_site.detaillotesite import getdetaillotesite

class TestDetalleLoteSite(unittest.TestCase):
    
    def test_get_detalle_lote(self):
        getDetalle = getdetaillotesite(1)
        self.assertIsNotNone(getDetalle,"error no existen dato")

if __name__ == '__main__':
    unittest.main()