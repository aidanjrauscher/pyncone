import pynecone as pc
from .pages import index
from .states import State

app = pc.App(state=State)
app.add_page(index)
app.compile()
