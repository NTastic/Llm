import torch
from transformers import pipeline
from app.config import settings

class LlamaModel:
    def __init__(self):
        self.pipeline = pipeline(
            "text-generation",
            model=settings.MODEL_PATH,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            model_kwargs={"quantization_config": {"load_in_4bit": True}}
        )

    async def generate(self, prompt, max_length=settings.MAX_LENGTH):
        outputs = self.pipeline(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            temperature=settings.TEMPERATURE,
            top_p=settings.TOP_P,
            do_sample=True
        )
        
        # The pipeline returns the full text including the prompt,
        # so we need to extract just the generated part
        generated_text = outputs[0]['generated_text']
        return generated_text[len(prompt):].strip()