import os
import sys
#import comfy.sd
#import comfy.utils
import folder_paths

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

class SK_embeddingStack:

    @classmethod
    def INPUT_TYPES(cls):
    
        embeddings = ["None"] + folder_paths.get_filename_list("embeddings")
        
        return {#"optional": {"textIn": ("STRING", {"default": "", "multiline": False, "forceInput": False},)},
                "required": {
                    #"textIn": ("STRING", {"default": "", "multiline": False, "forceInput": True},),
                    "embedding_1": ("BOOLEAN", {"default": False, "On": "enabled", "Off": "disabled"},),
                    "file_1": (embeddings,),
                    "weight_1": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01, "round": 0.001}),
                    "embedding_2": ("BOOLEAN", {"default": False, "On": "enabled", "Off": "disabled"},),
                    "file_2": (embeddings,),
                    "weight_2": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01, "round": 0.001}),
                    "embedding_3": ("BOOLEAN", {"default": False, "On": "enabled", "Off": "disabled"},),
                    "file_3": (embeddings,),
                    "weight_3": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01, "round": 0.001}),
                },
                "optional": {"STRING": ("STRING",{"default": "", "forceInput": True})}
                
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("textOut", )
    FUNCTION = "embedding_stacker"
    CATEGORY = "Skipper-Nodes"

    def __init__(self):
        self.default_text = "Escribe aquí tu texto..."

    def embedding_stacker(self, file_1, weight_1, embedding_1, file_2, weight_2, embedding_2, file_3, weight_3, embedding_3, STRING=None):

        if STRING is None:
            STRING = ""

        embeddings_list = STRING

        if file_1 != "None" and  embedding_1 == True:
            embeddings_list += ", (embedding:" + file_1 + ":" + str(weight_1) + "), "
        
        if file_2 != "None" and  embedding_2 == True:
            embeddings_list += ", (embedding:" + file_2 + ":" + str(weight_2) + "), "

        if file_3 != "None" and  embedding_3 == True:
            embeddings_list += ", (embedding:" + file_3 + ":" + str(weight_3) + "), "

        return (embeddings_list, )

