from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct")

def repondre_ia(message):
    prompt = f"<|user|>\n{message}\n<|assistant|>\n"
    inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=True)
    
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=100,
            temperature=0.7,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )
    
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Nettoyage de la sortie pour enlever le prompt initial
    return result.split("<|assistant|>")[-1].strip()
