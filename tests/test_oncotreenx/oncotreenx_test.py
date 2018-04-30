## imports
from oncotreenx import build_oncotree, get_basal, lookup_text

## testing classes
class TestOncotreenxConstruction:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

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
          g.node['BLOOD']['metanci'] == 'C12434'
          g.node['PT']['metanci'] == 'C7575'


class TestOncotreenxMethods:

    g = None

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup(self):
        self.g = build_oncotree(file_path="data/tumor_types.txt")

    def teardown(self):
        pass

    def test_get_basal(self):

        # get the ancestor.
        p = get_basal(self.g, "CCHDM")

        # make sure it is correct.
        assert 'BONE' == p

    def test_text_lu(self):

        # get the ancestor.
        p = lookup_text(self.g, "Adrenal Gland")

        # make sure it is correct.
        assert 'ADRENAL_GLAND' == p

