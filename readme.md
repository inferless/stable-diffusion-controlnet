# Stable Diffusion ControlNet
ControlNet is a neural network structure to control diffusion models by adding extra conditions. You can use this template to import it in Inferless.

## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the app.py according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

## Quick Start
Here is a quick start to get up and running the model on Inferless.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

Select PyTorch framework and choose **Repo(custom code)** as your model source and use the forked repo URL as the **Model URL**.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/github-custom-code) for more information on model import.

## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.

```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
                    "inputs":
                    [
                      {    
                        "name": "prompt",
                        "shape": [1],
                        "datatype": "BYTES",
                        "data":  ["Face of a yellow cat, high resolution, sitting on a park bench"]
                      },
                      {    
                        "name": "image_url",
                        "shape": [1],
                        "datatype": "BYTES",
                        "data":  ["https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"]
                      },
                      {    
                        "name": "control_url",
                        "shape": [1],
                        "datatype": "BYTES",
                        "data":  ["https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"]
                      },
                      {    
                        "name": "mask_url",
                        "shape": [1],
                        "datatype": "BYTES",
                        "data":  ["https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"]
                      }
                  ]
                }'
```

## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.pipe = None`.


For more information refer to the [Inferless docs](https://docs.inferless.com/).
