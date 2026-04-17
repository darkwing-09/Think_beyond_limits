""""https://colab.research.google.com
Click: New Notebook"""

!nvidia-smi
!pip install -q unsloth
!pip install -q xformers trl accelerate bitsandbytes datasets



from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/mistral-7b-bnb-4bit",
    max_seq_length = 2048,
    dtype = None,
    load_in_4bit = True,
)