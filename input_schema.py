INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Face of a yellow cat, high resolution, sitting on a park bench"]
    },
    "image_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"]
    },
    "control_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"]
    },
    "mask_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"]
    },
    
}
