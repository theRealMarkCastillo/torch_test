## A simple dev container that tests if Nvidia GPU is available in your container

## How to use
- In VS Code (or whatever you're using) load this repo remotely into a local Dev Container.
- Let the thing boot up
- Go in the terminal (or click the play button) and run:
```
vscode ➜ /workspaces/torch_test (main) $ /usr/local/bin/python /workspaces/torch_test/torch_example.py
```
You should see:
```
GPU is available
Tensor is on: cuda:0
```
