import base
import sys
import tdlib
import unittest

if(len(sys.argv)<2 or sys.argv[1]!="long"):
    sys.exit(77)

from graphs import *
import CFGs

#don't confuse python unittest
sys.argv=sys.argv[:1]

PREFIX = "CFGs"
COUNT = 1816

class TestTdLib_packages(unittest.TestCase):
    def test_MD(self):
        print("---MD---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T, w = tdlib.minDegree_decomp(G)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_boost_MD(self):
        print("---boost::MD---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T, w = tdlib.boost_minDegree_decomp(G)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_FI(self):
        print("---FI---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T, w = tdlib.fillIn_decomp(G)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_PP(self):
        print("---PP---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            G_, B, lb = tdlib.preprocessing(G)
            if G.vertices() is []:
                self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_PP_MD(self):
        print("---PP_MD---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T, w = tdlib.PP_MD(G)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_PP_FI(self):
        print("---PP_FI---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T, w = tdlib.PP_FI(G)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_PP_FI_TM(self):
        print("---PP_FI_TM---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T, w = tdlib.PP_FI_TM(G)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_MSVS_trivial(self):
        print("---MSVS_trivial---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T1, w1 = tdlib.trivial_decomposition(G)
            T2, w2 = tdlib.MSVS(G, T1)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T2), True)

    def test_minimalChordal_trivial(self):
        print("---minimalChordal_trivial---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T1, w1 = tdlib.trivial_decomposition(G)
            T2, w2 = tdlib.minimalChordal_decomp(G, T1)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T2), True)

    def test_seperator_algorithm(self):
        print("---seperator_algorithm---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T, w = tdlib.seperator_algorithm(G)
            self.assertEqual(tdlib.is_valid_treedecomposition(G, T), True)

    def test_conversion(self):
        print("---conversion---")
        for i in range(0, COUNT+1):
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))
            base.print_graph_name(PREFIX, i)
            T1, w1 = tdlib.minDegree_decomp(G)
            O = tdlib.treedec_to_ordering(T1)
            T2, w2 = tdlib.ordering_to_treedec(G, O)
            self.assertEqual(w1, w2)

if __name__ == '__main__':
    unittest.main()

# vim:ts=8:sw=4:et
