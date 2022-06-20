from dotenv import load_dotenv
from fastapi import FastAPI, Request
import os
from inference import inference
import os, fnmatch
load_dotenv()

app = FastAPI()

@app.get("/v1/getinference/{experiment_name}/{image}")
async def get_inference(request: Request, experiment_name: str, image: str):
    """
    > The function takes in a request, an experiment name, and an image, and returns the model outputs
    
    :param request: Request - this is the request object that is passed to the function
    :type request: Request
    :param experiment_name: The name of the experiment you want to run inference on
    :param image: The image to be classified
    :return: The model outputs are being returned.
    """
    model_outputs = inference(experiment_name, image)
    return model_outputs

@app.get("/v1/get_models")
async def get_models(request: Request):
    """
    It returns a list of all files in the `fashion_mnist_experiment` directory that start with
    `fashion_mnist_experiment`
    
    :param request: Request - the request object
    :type request: Request
    :return: A list of all the models in the fashion_mnist_experiment folder.
    """
    models = fnmatch.filter(os.listdir('./service/fashion_mnist_experiment'), 'fashion_mnist_experiment*')
    return models

@app.get("/v1/get_images")
async def get_models(request: Request):
    """
    It returns a list of all the PNG files in the `data` directory
    
    :param request: Request - this is the request object that is passed to the function
    :type request: Request
    :return: A list of images in the data folder
    """
    images = fnmatch.filter(os.listdir('./data'), '*.png')
    return images