import threading

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer


def main():
    local_model_dir = "./model/CodeRM-8B"

    tokenizer = AutoTokenizer.from_pretrained(local_model_dir, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        local_model_dir,
        trust_remote_code=True,
        torch_dtype=torch.float16 if torch.cuda.is_available() else None,
        device_map="auto" if torch.cuda.is_available() else None,
    )
    model.eval()

    messages = [{"role": "user", "content": "Who are you?"}]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    streamer = TextIteratorStreamer(
        tokenizer,
        skip_prompt=True,
        skip_special_tokens=True,
    )

    generation_kwargs = dict(
        **inputs,
        streamer=streamer,
        max_new_tokens=200,
        do_sample=False,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
    )

    t = threading.Thread(target=model.generate, kwargs=generation_kwargs)
    t.start()

    for text in streamer:
        print(text, end="", flush=True)
    print()  # newline
    t.join()


if __name__ == "__main__":
    main()