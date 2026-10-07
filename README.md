# Image to Video with Sound

A complete starter project for AI-driven image-to-video generation with generated sound design, voice synthesis, and cinematic video assembly. This repository provides the foundation for turning still images into animated clips with synchronized audio.

## Features

- Image-to-video orchestration
- Motion path generation and camera movement
- Sound generation hooks (music, ambience, voiceover)
- Audio and video assembly pipeline
- Mock pipeline for local testing and development
- CLI to generate sample media outputs

## Project Structure

```text
image-to-video-sound/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── examples/
│   └── basic_image_video.py
├── src/
│   └── image_to_video_sound/
│       ├── __init__.py
│       ├── audio.py
│       ├── cli.py
│       ├── config.py
│       ├── models.py
│       └── pipeline.py
└── tests/
    └── test_pipeline.py
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m image_to_video_sound.cli \
  --image assets/example.png \
  --prompt "A cinematic slow zoom into a portrait with atmospheric motion and subtle environmental sound" \
  --output output/final_video.mp4
```

## Core Workflow

1. Load source image
2. Build motion plan (zoom, pan, parallax)
3. Generate or attach audio (background ambience, voiceover, music)
4. Assemble video + audio into final MP4
5. Export result to disk

## Extending the Project

This repo is designed to integrate with:

- diffusion-based image animation backends
- speech synthesis APIs
- background music generation tools
- FFmpeg rendering pipelines

## Example Usage

```python
from image_to_video_sound.config import ImageVideoRequest
from image_to_video_sound.models import MockImageVideoModel
from image_to_video_sound.pipeline import ImageVideoPipeline

request = ImageVideoRequest(
    image_path="assets/example.png",
    prompt="Slow cinematic motion around the subject with ambient sound and gentle wind",
    duration_seconds=8,
    fps=24,
)

pipeline = ImageVideoPipeline(model=MockImageVideoModel(), output_dir="output")
result = pipeline.run(request, output_path="output/final_result.mp4")
print(result)
```

## License

MIT
