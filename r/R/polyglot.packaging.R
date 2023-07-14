#' @useDynLib polyglot.packaging, .registration = TRUE
#' @importFrom Rcpp evalCpp
NULL

#' @export
add_R <- function(a, b) {
    add_cpp(a, b)
}

#' @export
message_R <- function() {
    message_cpp()
}