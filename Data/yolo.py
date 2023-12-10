!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="m7pOg0Ed8py4ETHrAZcP")
project = rf.workspace("wawan-pradana").project("cinta_v2")
dataset = project.version(1).download("yolov8")
