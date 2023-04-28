from src.interaction import interaction, args_processing

if __name__ == "__main__":
    response = interaction()
    args_processing(response)