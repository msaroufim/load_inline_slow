#include <torch/extension.h>

torch::Tensor to_gray(torch::Tensor input);

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
m.def("to_gray", torch::wrap_pybind_function(to_gray), "to_gray");
}