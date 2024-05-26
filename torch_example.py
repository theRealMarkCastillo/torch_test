import torch

# Check if GPU is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU is available")
else:
    device = torch.device("cpu")
    print("GPU is not available")

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0], device=device)

# Print the device of the tensor
print("Tensor is on:", tensor.device)
