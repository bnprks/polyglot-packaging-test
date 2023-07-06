#include "cpp-core/add.hpp"
#include "cpp-core/message.hpp"

#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

PYBIND11_MODULE(cpp, m) {
    m.doc() = R"pbdoc(
        Pybind11 polyglot example plugin
        -----------------------

        .. currentmodule:: polyglot_packaging

        .. autosummary::
           :toctree: _generate

           add
           message
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers
    )pbdoc");

    m.def("message", &message, R"pbdoc(
        Give a message
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
