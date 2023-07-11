# Image-Generator
Image Generation Using stable diffusion (Pre-trained). Flexible to various Stable Diffusion versions. Can also be done using cpu and low end Gpu (instructions provided).
Requires atleast 4GB VRAM for mobile GPUs.

Here's how you can use for multiple versions of diffusions.

----> DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

----> DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base")

----> DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")

For Low end GPU's       Use .enable_vae_tiling()   or     Use .enable_xformers_memory_efficient_attention()

image_gen_model.enable_vae_tiling()


image_gen_model.enable_xformers_memory_efficient_attention()





For Cpu processing (Not Recommended)


Use .enable_model_cpu_offload()

image_gen_model.enable_model_cpu_offload()
