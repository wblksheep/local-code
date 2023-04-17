from client import RemoteTrainer
import retro

def main():
    game = "StreetFighterIISpecialChampionEdition-Genesis"
    state = "Champion.Level1.RyuVsGuile"
    env = retro.make(game, state)
    env.reset()

    remote_trainer = RemoteTrainer("http://192.168.50.1:5000")

    # 您可以通过这里的配置参数自定义 AI 训练过程
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
