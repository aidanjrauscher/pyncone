import pynecone as pc

class RandomgeneratorConfig(pc.Config):
    pass

config = RandomgeneratorConfig(
    app_name="random_generator",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)