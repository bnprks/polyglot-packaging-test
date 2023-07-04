// Generated by using Rcpp::compileAttributes() -> do not edit by hand
// Generator token: 10BE3573-1514-4C36-9D1C-5A225CD40393

#include <Rcpp.h>

using namespace Rcpp;

#ifdef RCPP_USE_GLOBAL_ROSTREAM
Rcpp::Rostream<true>&  Rcpp::Rcout = Rcpp::Rcpp_cout_get();
Rcpp::Rostream<false>& Rcpp::Rcerr = Rcpp::Rcpp_cerr_get();
#endif

// message_cpp
CharacterVector message_cpp();
RcppExport SEXP _polyglot_packaging_message_cpp() {
BEGIN_RCPP
    Rcpp::RObject rcpp_result_gen;
    Rcpp::RNGScope rcpp_rngScope_gen;
    rcpp_result_gen = Rcpp::wrap(message_cpp());
    return rcpp_result_gen;
END_RCPP
}
// add_cpp
int add_cpp(int a, int b);
RcppExport SEXP _polyglot_packaging_add_cpp(SEXP aSEXP, SEXP bSEXP) {
BEGIN_RCPP
    Rcpp::RObject rcpp_result_gen;
    Rcpp::RNGScope rcpp_rngScope_gen;
    Rcpp::traits::input_parameter< int >::type a(aSEXP);
    Rcpp::traits::input_parameter< int >::type b(bSEXP);
    rcpp_result_gen = Rcpp::wrap(add_cpp(a, b));
    return rcpp_result_gen;
END_RCPP
}

static const R_CallMethodDef CallEntries[] = {
    {"_polyglot_packaging_message_cpp", (DL_FUNC) &_polyglot_packaging_message_cpp, 0},
    {"_polyglot_packaging_add_cpp", (DL_FUNC) &_polyglot_packaging_add_cpp, 2},
    {NULL, NULL, 0}
};

RcppExport void R_init_polyglot_packaging(DllInfo *dll) {
    R_registerRoutines(dll, NULL, CallEntries, NULL, NULL);
    R_useDynamicSymbols(dll, FALSE);
}