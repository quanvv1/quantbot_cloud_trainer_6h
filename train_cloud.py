# Thin wrapper in case you prefer calling a single file locally or in other CI
import sys
from quantbot_research_lab.run_training import main

if __name__ == "__main__":
    # This delegates to the same CLI as run_training.py
    # Example: python train_cloud.py --episodes 60 --symbols "BTCUSDT,ETHUSDT,..."
    main()
