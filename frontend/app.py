import ast
from typing import List, Tuple

import gradio as gr
import pandas as pd
import psycopg2
import requests


class GradioOutputs:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="experiment_db",
            user="postgres",
            password="postgres",
            host="postgres",
            port="5432",
        )

    def model_result(self, experiment_name, image) -> str:
        """
        :param experiment_name: The name of the experiment you created in the previous step
        :param image: The image you want to classify
        """
        result = requests.get(
            f"http://backend.docker:8000/v1/getinference/{experiment_name}/{image}"
        )
        return result.text

    def models_list(self) -> List:
        """
        It returns a list of models.
        """
        result = requests.get(f"http://backend.docker:8000/v1/get_models")
        return ast.literal_eval(result.text)

    def images_list(self) -> List:
        """
        It returns a list of images.
        """
        result = requests.get(f"http://backend.docker:8000/v1/get_images")
        return ast.literal_eval(result.text)

    def training_result(self, experiment_name) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        :param experiment_name: The name of the experiment you want to get the results for
        """
        data = pd.read_sql_query(
            "select learning_rate, momentum, loss from experiment_data where experiment_name = %(value)s",
            self.connection,
            params={"value": experiment_name},
        )
        data = pd.concat(
            [data.drop(["loss"], axis=1), pd.DataFrame(ast.literal_eval(data["loss"][0]))], axis=1
        )
        return data[["Step", "Value"]], data


def main():
    go = GradioOutputs()
    models = go.models_list()
    images = go.images_list()
    gr.TabbedInterface(
        [
            gr.Interface(
                fn=go.model_result,
                inputs=[
                    gr.Dropdown(choices=models, value=models[0]),
                    gr.Dropdown(choices=images, value=images[0]),
                ],
                outputs="text",
            ),
            gr.Interface(
                fn=go.training_result,
                inputs=[gr.Dropdown(choices=models, value=models[0])],
                outputs=[gr.Timeseries(x="Step", y="Value"), gr.Dataframe()],
            ),
        ],
        tab_names=["model_inference", "training_metrics"],
    ).launch(server_port=8501, server_name="0.0.0.0")


if __name__ == "__main__":
    main()
