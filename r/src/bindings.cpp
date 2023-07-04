#include <Rcpp.h>
// [[Rcpp::plugins(cpp17)]]                                        

#include "cpp-core/add.hpp"
#include "cpp-core/message.hpp"

using namespace Rcpp;


// [[Rcpp::export]]
CharacterVector message_cpp() {
    return message();
}

// [[Rcpp::export]]
int add_cpp(int a, int b) {
    return add(a, b);
}