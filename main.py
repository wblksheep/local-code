from game.game_env import create_game_environment
from remote_training.remote_trainer import RemoteTrainer

def main():
    game, state = "StreetFighterIISpecialChampionEdition-Genesis", "Champion.Level1.RyuVsGuile"
    env = create_game_environment(game, state)
    env.reset()

    remote_trainer = RemoteTrainer("http://192.168.50.1:5000")

    config = {
        "learning_rate": 0.001,
        "num_epochs": 100,
        "batch_size": 64,
    }

    training_result = remote_trainer.start_training(config)
    print("Training result:", training_result)

    # 在这里编写与模拟器交互的代码以及使用训练好的 AI 模型进行游戏

if __name__ == "__main__":
    main()
