#include <torch/types.h>
#include <cuda.h>
#include <cuda_runtime.h>

#include <c10/core/TensorOptions.h>
#include <ATen/core/TensorBody.h>
#include <c10/util/ArrayRef.h>
torch::Tensor to_gray(torch::Tensor input) {
  auto output = torch::empty({input.size(0), input.size(1)}, input.options());  
  return output; 
}
