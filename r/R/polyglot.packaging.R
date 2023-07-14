#' @useDynLib polyglot.packaging, .registration = TRUE
#' @importFrom Rcpp evalCpp
NULL

#' Basic addition
#' @param a,b integers to add
#' @return Integer sum of inputs
#' @export
add_R <- function(a, b) {
    add_cpp(a, b)
}

#' Get a string from C++
#' @return Greeting message from C++
#' @export
message_R <- function() {
    message_cpp()
}