# Pre-Trained-Palmtree

This is a fork from the original [PalmTree library](https://github.com/palmtreemodel/PalmTree)

It is used to encode assembly sentences based on the palmtree trained transformer.

## Install

To install you should run:

```
pip install .
```

in the root directory of the repository.

## Usage

Encode the assebly basic block as follows:

```
from config import *
import eval_utils as utils


palmtree = utils.UsableTransformer(
    model_path="./palmtree/transformer.ep19", vocab_path="./palmtree/vocab"
)

# tokens has to be seperated by spaces.

text = [
    "mov rbp rdi",
    "mov ebx 0x1",
    "mov rdx rbx",
    "call memcpy",
    "mov [ rcx + rbx ] 0x0",
    "mov rcx rax",
    "mov [ rax ] 0x2e",
]

# it is better to make batches as large as possible.
embeddings = palmtree.encode(text)
print("usable embedding of this basicblock:", embeddings)
print("the shape of output tensor: ", embeddings.shape)
```