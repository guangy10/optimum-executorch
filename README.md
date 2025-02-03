<div align="center">

<img src="docs/assets/optimum-executorch.png" alt="Optimum ExecuTorch"/>

# 🤗 Optimum ExecuTorch

**Optimize and deploy Hugging Face models with ExecuTorch**

[Documentation](TBD) | [ExecuTorch](https://pytorch.org/executorch) | [Hugging Face](https://huggingface.co/)

</div>

## 🚀 Overview

Optimum ExecuTorch enables efficient deployment of transformer models using Meta's ExecuTorch framework. It provides:
- 🔄 Easy conversion of Hugging Face models to ExecuTorch format
- ⚡ Optimized inference with hardware-specific optimizations
- 🤝 Seamless integration with Hugging Face Transformers
- 📱 Efficient deployment on various devices

## ⚡ Quick Installation

Install from source:
```
git clone https://github.com/huggingface/optimum-executorch.git
cd optimum-executorch
pip install .
```

- 🔜 Install from pypi coming soon...

## 🎯 Quick Start

There are two ways to use Optimum ExecuTorch:

### Option 1: Export and Load Separately

#### Step 1: Export your model
Use the CLI tool to convert your model to ExecuTorch format:
```
optimum-cli export executorch \
    --model "meta-llama/Llama-3.2-1B" \
    --task "text-generation" \
    --recipe "xnnpack" \
    --output_dir="meta_llama3_2_1b"
```

#### Step 2: Load and run inference
Use the exported model for text generation:
```python
from optimum.executorch import ExecuTorchModelForCausalLM
from transformers import AutoTokenizer

# Load the exported model
model = ExecuTorchModelForCausalLM.from_pretrained(
    "./meta_llama3_2_1b",
    export=False
)

# Initialize tokenizer and generate text
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
generated_text = model.text_generation(
    tokenizer=tokenizer,
    prompt="Simply put, the theory of relativity states that"
)
```

### Option 2: Python API
```python
from optimum.executorch import ExecuTorchModelForCausalLM
from transformers import AutoTokenizer

# Load and export model in one step
model = ExecuTorchModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-1B",
    export=True,
    task="text-generation",
    recipe="xnnpack"
)

# Generate text right away
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
generated_text = model.text_generation(
    tokenizer=tokenizer,
    prompt="Simply put, the theory of relativity states that"
)
```

## 🛠️ Advanced Usage

Check our [ExecuTorch GitHub repo](https://github.com/pytorch/executorch) directly for:
- Custom model export configurations
- Performance optimization guides
- Deployment guides for Android, iOS, and embedded devices
- Additional examples

## 🤝 Contributing

We love your input! We want to make contributing to Optimum ExecuTorch as easy and transparent as possible. Check out our:

- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 📫 Get in Touch

- Report bugs through [GitHub Issues](https://github.com/huggingface/optimum-executorch/issues)
