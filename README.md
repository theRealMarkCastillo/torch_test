## A simple dev container that tests if Nvidia GPU is available in your container

## How to use
- In VS Code (or whatever you're using) load this repo remotely into a local Dev Container.
- Let the thing boot up
- Prompt should look like this:
```
vscode ➜ /workspaces/torch_test (main) $
```
- Go in the terminal (or click the play button) and run:
```
/usr/local/bin/python /workspaces/torch_test/torch_example.py
```
You should see:
```
GPU is available
Tensor is on: cuda:0
```
- If there is an error or says GPU Unavailable, then you either a) don't have a GPU instance or b) something corrupted in your dev container host c) Check your Nvidia driver version compatibility, CUDA version, etc.
  
