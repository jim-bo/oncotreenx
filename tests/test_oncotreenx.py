## imports
import unittest
from oncotreenx import build_oncotree, get_basal, name_to_code

## testing classes
class TestOncotreenxConstruction(unittest.TestCase):

    def test_build_oncotree_old(self):

        # build the tree.
        g = build_oncotree(file_path='data/tumor_types.old.txt')

        # assert we have some nodes.
        assert len(g.nodes()) > 10

    def test_build_oncotree(self):

        # build the tree.
        g = build_oncotree(file_path='data/tumor_types.txt')

        # assert we have some nodes.
        assert len(g.nodes()) > 10

    def test_ncit(self):

        # loop over tree type.
        for x in ['data/tumor_types.old.txt', 'data/tumor_types.txt']:
          
          # build the tree.
          g = build_oncotree(file_path=x)

          # spot check several values.
          g.nodes['BLOOD']['metanci'] == 'C12434'
          g.nodes['PT']['metanci'] == 'C7575'


class TestOncotreenxMethods(unittest.TestCase):


    def test_get_basal(self):

        # get the ancestor.
        g = build_oncotree(file_path="data/tumor_types.txt")
        p = get_basal(g, "CCHDM")

        # make sure it is correct.
        assert 'BONE' == p

    def test_text_lu(self):

        # get the ancestor.
        g = build_oncotree(file_path="data/tumor_types.txt")
        p = name_to_code(g, "Adrenal Gland")

        # make sure it is correct.
        assert 'ADRENAL_GLAND' == p