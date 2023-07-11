import torch
from diffusers import StableDiffusionPipeline
import random
class SD:
    device = "cuda" #use "cpu" if you don't have a gpu
    generator = torch.Generator(device)
    image_gen_steps = 50
    #image_gen_model_id = r"C:\Users\gokul\.cache\huggingface\hub\models--stabilityai--stable-diffusion-2-1\snapshots\845609e6cf0a060d8cd837297e5c169df5bff72c"
    image_size = (512,512)
    img_guidance_scale = 7.5




def generate_image(prompt,model):
    image = model(prompt,negative_prompt='artistic,cropped,ugly', num_inference_steps=SD.image_gen_steps,generator=SD.generator,guidance_scale=SD.image_gen_guidance_scale).images[0]
    image = image.resize(SD.image_size) #If you use a stable diffusion 2-1. It generates a 768x768 image . Other Diffusion Models generate 512x512.Here I resize 768x768 to a 512x512 size
    image.save('generated.png')
    return image

image_gen_model = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1",torch_dtype=torch.float16,use_auth_token='Your Hugging Face Token Here').to(SD.device)


#Here is an example of how you can use your local cache after the initial one time download of a model.

#image_gen_model = StableDiffusionPipeline.from_pretrained(r"C:\Users\gokul\.cache\huggingface\hub\models--stabilityai--stable-diffusion-2-1\snapshots\845609e6cf0a060d8cd837297e5c169df5bff72c",torch_dtype=torch.float16,use_auth_token='hugging_face_token_from_Huggingface_website').to(SD.device)

image_gen_model.enable_vae_tiling() #device Gpu with low Vram
#image_gen_model.enable_model_cpu_offload()  If device is cpu
prompt=input('Enter Your Prompt: ')


generate_image(prompt,image_gen_model)
