## imports
import unittest
from oncotreenx import build_oncotree, get_basal, name_to_code

## testing classes
class TestOncotreenxConstruction(unittest.TestCase):

    def setup(self):
        pass

    def teardown(self):
        pass

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

        # build graph
        g = build_oncotree(file_path="data/tumor_types.txt")

        # get the ancestor.
        p = get_basal(g, "CCHDM")

        # make sure it is correct.
        assert 'BONE' == p

    def test_name_to_node(self):

        # build graph
        g = build_oncotree(file_path="data/tumor_types.txt")

        # get the ancestor.
        for x, y in [\
            ('Appendiceal Adenocarcinoma', 'APAD'), 
            ('Encapsulated Glioma', 'ENCG'),
            ('Adrenal Gland', 'ADRENAL_GLAND')]:

            assert name_to_code(g, x) == y



