import pynecone as pc
from .pages import index
from .states import State



# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
