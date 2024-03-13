import json
from params.synthesis_params import SynthesisParams
from synthesizer import Synthesizer

from unith_thai.data_loaders.video.stream_video_reader import StreamVideoReader

from helpers.feature_loader import FeatureLoader

def run(params_path: str) -> None:
    print("Starting synthesis command!")
    with open(params_path) as f:
                print(f"Loading params from {params_path}...")
                params = SynthesisParams(**json.load(f))

    video_reader = StreamVideoReader(params.video_path, loop=False)

    print(f"Loading features from {params.features_path}...")
    feature_loader = FeatureLoader()
    features = feature_loader.load(params.features_path)

    synthesizer = Synthesizer(
        params.video_path,
        features,
        params.duration,
        params.intensity,
        params.use_last_w_pivots,
        video_reader,
        params.use_multi_id_training
        )
    
    print(f"Synthesizing {params.video_path}...")
    synthesizer.synthesize()
    
    return

if __name__ == "__main__":
    params_path = "/home/ubuntu/PTI/config_synthesis.json"
    run(params_path)