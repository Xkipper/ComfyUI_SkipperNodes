try:
    from .nodes.nodes_embedding import *
    from .nodes.nodes_textbox import *
except ImportError:
    print("\033[34mSkipper: \033[92mFailed to load Essential nodes\033[0m")

NODE_CLASS_MAPPINGS = { 
    "Embedding Stack": SK_embeddingStack,
    "Simple Box": SK_SimpleTxtBox,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Embedding Stack": "Skipper EmbeddingStack",
    "Simple Box": "Skipper SimpleTextBox",
}
