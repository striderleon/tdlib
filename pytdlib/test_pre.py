import tdlib
import unittest

from graphs import *

class TestTdLib_pre(unittest.TestCase):

    def test_preprocessing(self):
        V_, E_, B, lb = tdlib.preprocessing(V_P6, E_P6)
        self.assertEqual(V_, [])
        self.assertEqual(E_, [])
        self.assertEqual(len(B), 5)
        self.assertEqual(lb, 1)

        V_, E_, B, lb = tdlib.preprocessing(V_K5, E_K5)
        self.assertEqual(V_, [])
        self.assertEqual(E_, [])
        self.assertEqual(len(B), 4)
        self.assertEqual(lb, 4)

        V_, E_, B, lb = tdlib.preprocessing(V_Petersen, E_Petersen)
        self.assertEqual(V_, V_Petersen)
        self.assertEqual(E_, [0,1,0,4,0,5,1,2,1,6,2,3,2,7,3, \
                              4,3,8,4,9,5,7,5,8,6,8,6,9,7,9])
        self.assertEqual(len(B), 0)
        self.assertEqual(lb, 4)

    def test_PP_MD(self):
        V, E, w = tdlib.PP_MD(V_P6, E_P6)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_P6, E_P6, V, E) == 0, True)
        self.assertEqual(w, 1)

        V, E, w = tdlib.PP_MD(V_K5, E_K5)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_K5, E_K5, V, E) == 0, True)
        self.assertEqual(w, 4)

        V, E, w = tdlib.PP_MD(V_Petersen, E_Petersen)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_Petersen, E_Petersen, V, E) == 0, True)
        self.assertEqual(w >= 4 and w <= 5, True) #c++11 issuse

        V, E, w = tdlib.PP_MD(V_Pappus, E_Pappus)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_Pappus, E_Pappus, V, E) == 0, True)
        self.assertEqual(w, 6)

    def test_PP_FI_TM(self):
        V, E, w = tdlib.PP_FI_TM(V_P6, E_P6)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_P6, E_P6, V, E) == 0, True)
        self.assertEqual(w, 1)

        V, E, w = tdlib.PP_FI_TM(V_K5, E_K5)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_K5, E_K5, V, E) == 0, True)
        self.assertEqual(w, 4)

        V, E, w = tdlib.PP_FI_TM(V_Petersen, E_Petersen)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_Petersen, E_Petersen, V, E) == 0, True)
        self.assertEqual(w, 4)

        V, E, w = tdlib.PP_FI_TM(V_Pappus, E_Pappus)
        self.assertEqual(tdlib.is_valid_treedecomposition(V_Pappus, E_Pappus, V, E) == 0, True)
        self.assertEqual(w, 6)


if __name__ == '__main__':
    unittest.main()
