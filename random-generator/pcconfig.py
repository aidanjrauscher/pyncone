import pynecone as pc

class RandomgeneratorConfig(pc.Config):
    pass

config = pc.Config(
    app_name="random_generator",
    api_url="0.0.0.0:8000",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
)