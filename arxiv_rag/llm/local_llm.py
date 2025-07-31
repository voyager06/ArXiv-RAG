from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

class OpenSourceLLM:
    def __init__(self, model_name: str = "microsoft/phi-2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            trust_remote_code=True
        ).to("cpu")  # ✅ Explicitly move to CPU

        self.device = torch.device("cpu")  # ✅ Define self.device for later use

        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=-1  # ✅ -1 means CPU in pipelines
        )

    def generate_response(self, context: str, question: str, max_new_tokens=512):
        formatted_prompt = (
            f"Based on the following context, answer the question.\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{question}\n\n"
            f"Answer:"
        )

        # Tokenize prompt and truncate if necessary
        inputs = self.tokenizer(
            formatted_prompt,
            return_tensors="pt",
            truncation=True,
            max_length=self.model.config.max_position_embeddings - max_new_tokens,
        )
        
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.7,
                eos_token_id=self.tokenizer.eos_token_id or 50256,
                pad_token_id=self.tokenizer.pad_token_id or self.tokenizer.eos_token_id or 50256
            )

        output_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Optional cleanup
        if formatted_prompt in output_text:
            output_text = output_text.replace(formatted_prompt, "").strip()

        return output_text
