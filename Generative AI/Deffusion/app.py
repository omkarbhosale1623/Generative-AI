from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda")  # if you have GPU

prompt = "A futuristic cityscape at sunset"
image = pipe(prompt).images[0]

image.show()
