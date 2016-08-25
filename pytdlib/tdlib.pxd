from libcpp.vector cimport vector
from libcpp cimport bool

cdef extern from "python_tdlib.hpp":

##############################################################
############ PREPROCESSING ###################################

    int gc_preprocessing(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                         vector[vector[int]] &bags, int lb)
    int gc_PP_MD(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                 vector[vector[int]] &V_T, vector[unsigned int] &E_T, int lb)
    int gc_PP_FI_TM(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                    vector[vector[int]] &V_T, vector[unsigned int] &E_T, int lb)

##############################################################
############ LOWER BOUNDS ####################################

    int gc_deltaC_min_d(vector[unsigned int] &V, vector[unsigned int] &E)
    int gc_deltaC_max_d(vector[unsigned int] &V, vector[unsigned int] &E)
    int gc_deltaC_least_c(vector[unsigned int] &V, vector[unsigned int] &E)

    int gc_LBN_deltaC(vector[unsigned int] &V, vector[unsigned int] &E)
    int gc_LBNC_deltaC(vector[unsigned int] &V, vector[unsigned int] &E)
    int gc_LBP_deltaC(vector[unsigned int] &V, vector[unsigned int] &E)
    int gc_LBPC_deltaC(vector[unsigned int] &V, vector[unsigned int] &E)

##############################################################
############ EXACT ALGORITHMS ################################

    int gc_exact_decomposition_cutset(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                      vector[vector[int]] &V_T, vector[unsigned int] &E_T, int lb)
    int gc_exact_decomposition_cutset_decision(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                      vector[vector[int]] &V_T, vector[unsigned int] &E_T, int k)
    int gc_exact_decomposition_dynamic(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                      vector[vector[int]] &V_T, vector[unsigned int] &E_T, int lb)
    #int gc_exact_decomposition_branch_and_bound(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
    #                                            vector[vector[int]] &V_T, vector[unsigned int] &E_T, int lb)

##############################################################
############ APPROXIMATIVE ALGORITHMS ########################

    int gc_seperator_algorithm(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                vector[vector[int]] &V_T, vector[unsigned int] &E_T)
    void gc_minDegree_decomp(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                               vector[vector[int]] &V_T, vector[unsigned int] &E_T)
    void gc_boost_minDegree_decomp(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                               vector[vector[int]] &V_T, vector[unsigned int] &E_T)
    void gc_fillIn_decomp(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                            vector[vector[int]] &V_T, vector[unsigned int] &E_T)
    void gc_minDegree_ordering(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                               vector[unsigned int] &elim_ordering)
    void gc_fillIn_ordering(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                            vector[unsigned int] &elim_ordering)
    #int gc_random_branch_and_bound(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
    #                        vector[vector[int]] &V_T, vector[unsigned int] &E_T, int lb)
    #int gc_random_elimination_orderings(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
    #                                    vector[vector[int]] &V_T, vector[unsigned int] &E_T, int lb)

##############################################################
############ POSTPROCESSING ##################################

    int gc_MSVS(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                vector[vector[int]] &V_T, vector[unsigned int] &E_T)

    void gc_minimalChordal(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                           vector[unsigned int] &old_elimination_ordering,
                           vector[unsigned int] &new_elimination_ordering)

##############################################################
############ APPLICATIONS ####################################

    void gc_max_clique_with_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                              vector[vector[int]] &V_T, vector[unsigned int] &E_T,
                                              vector[unsigned int] &C)
    void gc_max_independent_set_with_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                                       vector[vector[int]] &V_T, vector[unsigned int] &E_T,
                                                       vector[unsigned int] &IS)
    void gc_min_vertex_cover_with_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                                    vector[vector[int]] &V_T, vector[unsigned int] &E_T,
                                                    vector[unsigned int] &VC)
    void gc_min_coloring_with_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                                    vector[vector[int]] &V_T, vector[unsigned int] &E_T,
                                                    vector[vector[int]] &col)

    void gc_min_dominating_set_with_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                                       vector[vector[int]] &V_T, vector[unsigned int] &E_T,
                                                       vector[unsigned int] &DS)

    #void gc_min_feedback_vertex_set_with_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
    #                                                   vector[vector[int]] &V_T, vector[unsigned int] &E_T,
    #                                                   vector[unsigned int] &FVS)

##############################################################
############ MISC ############################################

    int gc_ordering_to_treedec(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                               vector[vector[int]] &V_T, vector[unsigned int] &E_T,
                               vector[unsigned int] &elim_ordering)
    void gc_treedec_to_ordering(vector[vector[int]] &V, vector[unsigned int] &E,
                                vector[unsigned int] &elim_ordering);
    int gc_is_valid_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                      vector[vector[int]] &V_T, vector[unsigned int] &E_T)
    void gc_trivial_decomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                  vector[vector[int]] &V_T, vector[unsigned int] &E_T)
    int gc_get_width(vector[vector[int]] &V_T)


