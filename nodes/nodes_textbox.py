
class SK_SimpleTxtBox:

    @classmethod
    def INPUT_TYPES(cls):
        
        return {
                "required": {
                    "Text": ("STRING", {"default": "", "multiline": True,},),
                },
                "optional": {"STRING": ("STRING",{"default": "", "forceInput": True})}
                
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("textOut", )
    FUNCTION = "text_link"
    CATEGORY = "Skipper-Nodes"

    def __init__(self):
        self.default_text = "Escribe aquí tu texto..."

    def text_link(self, Text, STRING=None):

        if STRING is None:
            STRING = ""

        txt = STRING
        txt += ", " + Text

        return (txt, )

