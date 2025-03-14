import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"]='1'
from huggingface_hub import snapshot_download
import PIL
import requests
import torch
import base64
from io import BytesIO
from diffusers import ControlNetModel, UniPCMultistepScheduler
from controlnet_inpaint import StableDiffusionControlNetInpaintPipeline


class InferlessPythonModel:
    def download_image(url):
        response = requests.get(url)
        return PIL.Image.open(BytesIO(response.content)).convert("RGB")

    def initialize(self):
        model_id = "stable-diffusion-v1-5/stable-diffusion-inpainting"
        snapshot_download(repo_id=model_id,allow_patterns=["*.ckpt"])
        controlnet = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16)
        self.pipe = StableDiffusionControlNetInpaintPipeline.from_pretrained( model_id,controlnet=controlnet,torch_dtype=torch.float16)

        # speed up diffusion process with faster scheduler and memory optimization
        self.pipe.scheduler = UniPCMultistepScheduler.from_config(self.pipe.scheduler.config)
        self.pipe = self.pipe.to("cuda:0")

    def infer(self, inputs):
        prompt = inputs["prompt"]
        image_url = inputs["image_url"]
        mask_url = inputs["mask_url"]
        control_url = inputs["control_url"]
        
        init_image = InferlessPythonModel.download_image(image_url).resize((512, 512))
        mask_image = InferlessPythonModel.download_image(mask_url).resize((512, 512))
        control_image = InferlessPythonModel.download_image(control_url).resize((512, 512))
        generator = torch.manual_seed(0)
        inpaint_image = self.pipe(
            prompt=prompt, 
            num_inference_steps=20,
            generator=generator,
            image=init_image,
            controlnet_conditioning_image=control_image, 
            mask_image=mask_image,
        ).images[0]
        
        buff = BytesIO()
        inpaint_image.save(buff, format="PNG")
        img_str = base64.b64encode(buff.getvalue()).decode()
        print("type-->", type(img_str), flush=True)
        return {"generated_image_base64": img_str}

    def finalize(self):
        self.pipe = None
